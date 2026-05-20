from fastapi import FastAPI, HTTPException, Request, Depends, Header
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.models import CodeInput, AnalysisResponse, FeedbackItem, ComplexityMetrics
from app.analyzers.pylint_analyzer import PylintAnalyzer
from app.analyzers.radon_analyzer import RadonAnalyzer
from app.analyzers.rule_engine import RuleEngine

# Auth imports
from app.database import SessionLocal, User, CodeHistory, AIExplanation
from app.auth import (
    get_password_hash, 
    verify_password, 
    create_access_token, 
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
import sys
import os
sys.path.append('..')
sys.path.append('.')

# Add parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


# REST API Initialization
app = FastAPI(title="DevNest API", version="1.0.0")

# Enable CORS - CRITICAL for frontend to connect!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize analyzers (Processes Requested)
pylint_analyzer = PylintAnalyzer()
radon_analyzer = RadonAnalyzer()
rule_engine = RuleEngine()



# Health Check Endpoint - GET METHOD
@app.get("/")
async def root():
    return {"message": "DevNest API is running!", "status": "healthy"}


# Code Analysis Endpoint - POST METHOD
# This endpoint accepts code input and returns analysis results
# Main REST API endpoint for code analysis

@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_code(
    input_data: CodeInput, 
    db: Session = Depends(get_db),
    authorization: Optional[str] = Header(None)
):
    try:
        code = input_data.code
        
        if not code.strip():
            raise HTTPException(status_code=400, detail="Code cannot be empty")
        
        # Analyze complexity with Radon
        complexity_data = radon_analyzer.analyze(code)
        
        # Detect issues with Pylint
        pylint_issues = pylint_analyzer.analyze(code)
        
        # Translate issues using Rule Engine
        feedback_items = []
        seen_codes = {}  # Track codes to deduplicate
        
        # Define which codes should be deduplicated (show first occurrence only)
        DEDUPLICATE_CODES = {
            # Conventions - Show first occurrence only
            'C0103',  # Naming convention
            'C0114',  # Missing module docstring
            'C0116',  # Missing function docstring  
            'C0301',  # Line too long
            'C0121',  # Singleton comparison (== True)
            'C0123',  # Use isinstance()
            'C0200',  # Consider using enumerate
            'C0201',  # Consider iterating dictionary
            'C0325',  # Unnecessary parens
            
            # Warnings - Deduplicate similar types
            'W0104',  # Redefined builtin
            'W0631',  # Undefined loop variable
            
            # Refactors - Deduplicate similar patterns
            'R1705',  # Unnecessary else after return
            'R1720',  # No else after raise
            'R1732',  # Consider using with (context manager)
        }
        
        for issue in pylint_issues:
            translated = rule_engine.translate_message(
                error_code=issue['code'],
                line=issue['line'],
                symbol=issue.get('symbol')
            )
            
            error_code = issue['code']
            
            # Check if this code should be deduplicated
            if error_code in DEDUPLICATE_CODES:
                if error_code in seen_codes:
                    # Skip duplicate - already shown
                    print(f"⏭️  Skipping duplicate {error_code} on line {issue['line']} (already shown on line {seen_codes[error_code]})")
                    continue
                seen_codes[error_code] = issue['line']
            
            # ✅ FIX: Determine correct type based on Pylint code prefix
            correct_type = translated.get('type', 'error')  # Default from rule_engine
            
            if error_code.startswith('E'):
                correct_type = 'error'
            elif error_code.startswith('W'):
                correct_type = 'warning'
            elif error_code.startswith('C'):
                correct_type = 'convention'
            elif error_code.startswith('R'):
                correct_type = 'refactor'
            elif error_code.startswith('F'):
                correct_type = 'error'  # Fatal = error
            
            # Override the type with correct value
            translated['type'] = correct_type
            
            print(f"📝 Code {error_code} → Type: {correct_type}")
            
            feedback_items.append(FeedbackItem(**translated))
        
        # Add optimizations suggestions
        code_lines = input_data.code.split('\n')
        optimizations = rule_engine.add_optimization_suggestions(code_lines)
        
        print(f"✅ Found {len(optimizations)} optimization suggestions")
        
        for opt in optimizations:
            try:
                # Format optimization message with structured sections
                message = f"{opt.get('title', 'Optimization Suggestion')}\n"
                message += "━" * 40 + "\n\n"
                message += f"📋 WHAT'S WRONG:\n{opt.get('explain', '')}\n\n"
                message += f"🔧 HOW TO FIX:\n{opt.get('how_to_fix', '')}\n\n"
                message += "📝 EXAMPLE:\n\n"
                message += f"❌ WRONG:\n{opt.get('wrong', '')}\n\n"
                message += f"✅ RIGHT:\n{opt.get('right', '')}\n\n"
                message += f"📚 LEARN MORE:\n{opt.get('learn', '')}"
                
                # Convert to FeedbackItem format
                feedback_item = FeedbackItem(
                    type=opt.get('severity', 'optimization'),
                    line=opt['line'],
                    code='OPT',
                    message=message
                )
                
                feedback_items.append(feedback_item)
                print(f"  ✓ Added optimization: {opt.get('title', 'Unknown')} at line {opt['line']}")
                
            except Exception as e:
                print(f"  ❌ Error adding optimization: {e}")
                print(f"     Optimization data: {opt}")
        
        # Sort feedback items by priority
        # Priority order: Error → Warning → Optimization → Convention → Refactor
        def get_priority(item):
            """Return priority number for sorting (lower = higher priority)"""
            type_lower = item.type.lower()
            
            if 'error' in type_lower:
                return 1  # Highest priority
            elif 'warning' in type_lower:
                return 2
            elif 'optimization' in type_lower:
                return 3
            elif 'convention' in type_lower:
                return 4
            elif 'refactor' in type_lower:
                return 5
            else:
                return 6  # Unknown types go last
        
        # Sort by priority, then by line number within same priority
        feedback_items = sorted(feedback_items, key=lambda x: (get_priority(x), x.line))
        
        print(f"📊 Feedback sorted by priority: {len(feedback_items)} items")

        # Prepare response
        try:
            print(f"[DEBUG] Creating response with {len(feedback_items)} sorted feedback items")
            print(f"[DEBUG] Complexity data: {complexity_data}")
            
            response = AnalysisResponse(
                success=True,
                complexity=ComplexityMetrics(**complexity_data),
                feedback=feedback_items
            )
            print(f"[DEBUG] Response created successfully")
        except Exception as e:
            print(f"❌ ERROR creating AnalysisResponse: {e}")
            import traceback
            traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Error creating response: {str(e)}")
        
        # Save to history if logged in
        print(f"DEBUG: Authorization header present: {authorization is not None}")
        if authorization and authorization.startswith('Bearer '):
            try:
                from jose import jwt, JWTError
                from app.auth import SECRET_KEY, ALGORITHM
                import json
                
                token = authorization.replace('Bearer ', '')
                print(f"DEBUG: Token extracted, length: {len(token)}")
                
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                username = payload.get('sub')
                print(f"DEBUG: Username from token: {username}")
                
                if username:
                    user = db.query(User).filter(User.username == username).first()
                    if user:
                        print(f"DEBUG: User found! ID: {user.id}, Username: {user.username}")
                        
                        try:
                            history_entry = CodeHistory(
                                user_id=user.id,
                                code=code,
                                analysis_result=json.dumps({
                                    'complexity': complexity_data,
                                    'total_feedback': len(feedback_items),
                                    'errors': len([item for item in feedback_items if 'error' in item.type.lower()]),
                                    'warnings': len([item for item in feedback_items if 'warning' in item.type.lower()]),
                                    'optimizations': len([item for item in feedback_items if 'optimization' in item.type.lower()]),
                                    'conventions': len([item for item in feedback_items if 'convention' in item.type.lower()]),
                                    'refactors': len([item for item in feedback_items if 'refactor' in item.type.lower()])
                                }),
                                ai_feedback=json.dumps([{
                                    'type': item.type,
                                    'line': item.line,
                                    'message': item.message,
                                    'code': item.code
                                } for item in feedback_items])
                            )
                            db.add(history_entry)
                            db.commit()
                            db.refresh(history_entry)
                            print(f"✅ SUCCESS: History saved! Entry ID: {history_entry.id}")
                        except Exception as hist_error:
                            print(f"❌ ERROR saving history: {hist_error}")
                            import traceback
                            traceback.print_exc()
                            # Don't fail the whole request if history fails
                    else:
                        print(f"❌ ERROR: User '{username}' not found in database")
                else:
                    print(f"❌ ERROR: No username found in token payload")
                    
            except JWTError as e:
                print(f"❌ JWT ERROR: {str(e)}")
            except Exception as e:
                print(f"❌ HISTORY SAVE ERROR: {str(e)}")
                import traceback
                traceback.print_exc()
        else:
            print(f"DEBUG: No valid authorization header (not logged in)")
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/api/history")
async def get_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get user's code analysis history"""
    print(f"[DEBUG] GET /api/history called - ENDPOINT 1 - User: {current_user.username}")
    """Get user's code analysis history"""
    try:
        
        # Get user's history, most recent first
        history = db.query(CodeHistory).filter(
            CodeHistory.user_id == current_user.id
        ).order_by(CodeHistory.created_at.desc()).limit(50).all()
        
        import json
        history_data = []
        for entry in history:
            history_data.append({
                'id': entry.id,
                'code': entry.code,
                'analysis_result': json.loads(entry.analysis_result) if entry.analysis_result else {},
                'created_at': entry.created_at.isoformat() + 'Z',  # Add Z to indicate UTC
            })
        
        return {
            'username': current_user.username,
            'history': history_data
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# Create History for individual users 
@app.get("/api/history/{history_id}")
async def get_history_detail(history_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Get detailed analysis from history"""
    try:
       
        # Get specific history entry
        entry = db.query(CodeHistory).filter(
            CodeHistory.id == history_id,
            CodeHistory.user_id == current_user.id
        ).first()
        
        if not entry:
            raise HTTPException(status_code=404, detail="History entry not found")
        
        import json
        return {
            'id': entry.id,
            'code': entry.code,
            'analysis_result': json.loads(entry.analysis_result) if entry.analysis_result else {},
            'feedback': json.loads(entry.ai_feedback) if entry.ai_feedback else [],
            'created_at': entry.created_at.isoformat() + 'Z',
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/history/clear-all")
async def clear_all_code_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Clear all code analysis history for current user"""
    try:
        print(f"[DEBUG] Clear all code history - User: {current_user.username}")
        
        deleted = db.query(CodeHistory).filter(
            CodeHistory.user_id == current_user.id
        ).delete()
        
        db.commit()
        
        return {
            "success": True,
            "deleted_count": deleted,
            "message": f"Deleted {deleted} analysis entries"
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
# ========================================
# AI EXPLANATION ENDPOINT
# ========================================

import requests
import time
import re

# Ollama Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5-coder:1.5b-instruct"

@app.post("/api/ai-explain")
async def ai_explain(input_data: CodeInput):
    """
    AI explains code using Qwen2.5-Coder 1.5B
    Optimized for consistent, student-friendly feedback
    """
    try:
        code = input_data.code
        
        if not code.strip():
            raise HTTPException(status_code=400, detail="Code cannot be empty")
        
        # EDUCATIONAL PROMPT - Detailed explanations for learning
        # OPTIMIZED PROMPT FOR 1.5B MODEL - Clean output
        prompt = f"""<|im_start|>system
You are a Python code analyzer. You MUST follow the exact format. Never put errors in the "GOOD PRACTICES FOUND" section.
<|im_end|>
<|im_start|>user
Analyze this Python code:
```python
{code}
```

Follow this EXACT format. Do NOT mix up or skip sections:

WHAT YOUR CODE DOES:
[Explain what the code attempts to do in 2-3 sentences]

GOOD PRACTICES FOUND:
[ONLY list POSITIVE things the code does well. If nothing good, write "The code structure is clear"]

ISSUES TO FIX:

CRITICAL ERRORS:
[List ALL errors and problems here. NOT in good practices section]

STYLE IMPROVEMENTS:
[Suggest improvements or write "Code can be improved with error handling"]

LEARNING TIPS:
- [One practical tip about error handling or best practices]

KEY TAKEAWAY:
[One sentence about what to learn from this code]

CRITICAL RULES:
1. NEVER put errors in "GOOD PRACTICES FOUND" section
2. Put ALL problems under "CRITICAL ERRORS" or "ISSUES TO FIX"
3. "GOOD PRACTICES" = only positive things
4. Complete ALL sections
5. NO line breaks within numbered items
<|im_end|>
<|im_start|>assistant

"""

        print(f"\n{'='*60}")
        print("🤖 AI Analysis Request - Ollama Qwen2.5")
        print(f"{'='*60}")
        print(f"Code length: {len(code)} characters")
        print("Sending to Ollama...")
        
        start_time = time.time()
        
       # OPTIMIZED FOR 1.5B MODEL - Fast and efficient
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {

                # Optimized for 1.5B model speed
                "temperature": 0.3,       # Slightly higher for creativity
                "top_p": 0.9,             # Good balance
                "top_k": 40,              # Reasonable choices
                "num_predict": 900,       # Shorter for 1.5B (was 2000)
                "min_p": 0.05,            # Ensure minimum quality
                "num_ctx": 2048,          # Sufficient context
                "mirostat": 2,            # Forces consistent output
                "mirostat_tau": 5.0,      # Consistency level
                "mirostat_eta": 0.1,

                # CPU optimization for i7
                "num_thread": 6,          # 6 threads for i7
                "num_batch": 256,         # Smaller batch for 1.5B
                
                # Quality controls
                "repeat_penalty": 1.2,    # Prevent repetition
                "repeat_last_n": 64,
                
                # Stop tokens
                "stop": [
                    "<|im_end|>"
                ],
                
                # Memory
                "numa": False,
                "num_keep": 8,
            },
            "keep_alive": "30m"  # Keep loaded 30 minutes
        }
        
        # Send request to Ollama
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120  # Longer timeout for detailed responses (was 90)
        )
        
        elapsed = time.time() - start_time
        
        print(f"Response status: {response.status_code}")
        print(f"Response time: {elapsed:.1f} seconds")
        
        if response.status_code != 200:
            print(f"❌ Ollama Error: Status {response.status_code}")
            print(f"Response: {response.text}")
            raise HTTPException(
                status_code=503,
                detail="Ollama service error. Make sure Ollama is running: 'ollama serve'"
            )
        
        result = response.json()
        ai_explanation = result.get('response', '').strip()
        
        # Clean up leaked prompt instructions
        leaked_phrases = [
            r'\[Suggest improvements or write[^\]]*\]',
            r'\[list errors or say[^\]]*\]',
            r'\[explanation\]',
            r'\[list good things[^\]]*\]',
            r'\[Explain[^\]]*\]',
            r'\[ONLY[^\]]*\]',
            r'\[give suggestions[^\]]*\]',
            r'\[Practical tip[^\]]*\]',
            r'\[One sentence[^\]]*\]',
            r'\[.*?or write.*?\]',
            r'\[.*?or say.*?\]',
        ]
        
        for pattern in leaked_phrases:
            ai_explanation = re.sub(pattern, '', ai_explanation, flags=re.IGNORECASE)
        
        # Remove any remaining brackets with instructions
        ai_explanation = re.sub(r'\[.*?\]', '', ai_explanation)
        
        # Clean up double spaces
        ai_explanation = re.sub(r'\s+', ' ', ai_explanation)
        ai_explanation = ai_explanation.strip()

        # Validate response quality
        if not ai_explanation:
            raise HTTPException(
                status_code=500,
                detail="AI returned empty response. Try again."
            )

        # Clean up markdown symbols
        ai_explanation = ai_explanation.replace('###', '')
        ai_explanation = ai_explanation.replace('##', '')
        ai_explanation = ai_explanation.replace('#', '')
        
        # Validate complete response
        required = ['WHAT YOUR CODE DOES:', 'GOOD PRACTICES FOUND:', 'KEY TAKEAWAY:']
        missing = [s for s in required if s not in ai_explanation]
        
        if missing:
            print(f"⚠️ Incomplete response. Missing: {missing}")
            ai_explanation += f"\n\n[Note: Analysis may be incomplete]"

         # VALIDATION - Check if response is complete
        required_sections = [
            'WHAT YOUR CODE DOES:',
            'GOOD PRACTICES FOUND:',
            'ISSUES TO FIX:',
            'LEARNING TIPS:',
            'KEY TAKEAWAY:'
        ]

        missing_sections = [s for s in required_sections if s not in ai_explanation]
        
        if missing_sections:
            print(f"⚠️ WARNING: Incomplete response. Missing: {missing_sections}")
            # Optionally retry or append missing sections notice

            # After all validation and cleanup
            return {
                "success": True,
                "explanation": ai_explanation,
                "model": "Qwen2.5-Coder 1.5B",
                "response_time": elapsed
            }
        
        
        # Clean up markdown symbols
        ai_explanation = ai_explanation.replace('###', '')
        ai_explanation = ai_explanation.replace('##', '')
        ai_explanation = ai_explanation.replace('#', '')
        ai_explanation = ai_explanation.replace("-"," ")


        # Validate response quality
        if not ai_explanation:
            raise HTTPException(
                status_code=500,
                detail="AI returned empty response. Try again."
            )
        
        if len(ai_explanation) < 200:  # Increased from 100 for detailed responses
            print(f"⚠️ Warning: Short response ({len(ai_explanation)} chars)")
            print(f"Response: {ai_explanation}")
        
        # Check if response follows format (no emojis, just headers)
        has_structure = (
            'WHAT YOUR CODE DOES' in ai_explanation or 
            'GOOD PRACTICES' in ai_explanation or
            'ISSUES TO FIX' in ai_explanation
        )
        
        if not has_structure:
            print("⚠️ Warning: Response doesn't follow expected format")
            print(f"First 300 chars: {ai_explanation[:300]}")
        
        print(f"✅ AI Response Received")
        print(f"Response length: {len(ai_explanation)} characters")
        print(f"Words: ~{len(ai_explanation.split())} words")
        print(f"Has expected structure: {has_structure}")
        print(f"{'='*60}\n")
        
        return {
            "success": True,
            "explanation": ai_explanation,
            "model": "Qwen2.5-Coder 1.5B (Ollama)",
            "response_time": elapsed
        }
        
    except requests.exceptions.Timeout:
        print("⏰ Timeout: Request took too long")
        raise HTTPException(
            status_code=504,
            detail="AI response timeout (>120s). The model may be loading. Try again."
        )
    
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Cannot reach Ollama")
        raise HTTPException(
            status_code=503,
            detail="Cannot connect to Ollama. Make sure Ollama is running: 'ollama serve'"
        )
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/ai-status")
async def check_ai_status():
    """
    Health check for Ollama AI service
    Also pre-loads the model if not loaded
    """
    try:
        # Check if Ollama is running
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        
        if response.status_code == 200:
            models_data = response.json()
            models = models_data.get('models', [])
            model_names = [m.get('name', '') for m in models]
            
            has_qwen = any('qwen2.5-coder:1.5B' in name for name in model_names)
            
            if has_qwen:
                # PRE-LOAD MODEL - Makes first request faster!
                print("Pre-loading Qwen2.5-Coder model...")
                try:
                    requests.post(
                        "http://localhost:11434/api/generate",
                        json={
                            "model": OLLAMA_MODEL,
                            "prompt": "test",
                            "stream": False,
                            "options": {"num_predict": 1},
                            "keep_alive": "5m"
                        },
                        timeout=10
                    )
                    print("✅ Model pre-loaded successfully")
                except:
                    print("⚠️ Model pre-load skipped")
                
                return {
                    "status": "online",
                    "ollama_running": True,
                    "model": OLLAMA_MODEL,
                    "model_available": True,
                    "model_preloaded": True,
                    "message": "✅ AI is ready! Model is pre-loaded in memory.",
                    "expected_response_time": "10-20 seconds (detailed educational feedback)"
                }
            else:
                return {
                    "status": "model_not_found",
                    "ollama_running": True,
                    "model": OLLAMA_MODEL,
                    "model_available": False,
                    "message": f"❌ Model not found. Download it: ollama pull qwen2.5-coder:1.5b-instruct",
                    "available_models": model_names
                }
        else:
            return {
                "status": "error",
                "ollama_running": False,
                "message": "❌ Ollama service error"
            }
            
    except requests.exceptions.ConnectionError:
        return {
            "status": "offline",
            "ollama_running": False,
            "message": "❌ Ollama is not running. Start it: 'ollama serve'"
        }
    except Exception as e:
        return {
            "status": "error",
            "ollama_running": False,
            "message": f"Error: {str(e)}"
        }
    

# ========================================
# STARTUP EVENT - PRE-LOAD MODEL
# ========================================

@app.on_event("startup")
async def startup_event():
    """
    Pre-load model on startup for speed
    """
    print("\n" + "="*60)
    print("🚀 DevNest Starting - Speed Optimized")
    print("="*60)
    
    try:
        print("🔍 Checking Ollama...")
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        
        if response.status_code == 200:
            print("✅ Ollama running")
            
            models_data = response.json()
            models = models_data.get('models', [])
            model_names = [m.get('name', '') for m in models]
            
            has_qwen = any('qwen2.5-coder:1.5B' in name for name in model_names)
            
            if has_qwen:
                print(f"✅ Qwen 1.5B found")
                print("⏳ Pre-loading model into RAM (3 times for stability)...")
                
                # Load 3 times to ensure it stays in RAM
                for i in range(3):
                    try:
                        preload = requests.post(
                            "http://localhost:11434/api/generate",
                            json={
                                "model": OLLAMA_MODEL,
                                "prompt": f"test{i}",
                                "stream": False,
                                "options": {
                                    "num_predict": 1,
                                    "num_ctx": 512
                                },
                                "keep_alive": "30m"
                            },
                            timeout=30
                        )
                        
                        if preload.status_code == 200:
                            print(f"  ✓ Pre-load {i+1}/3 successful")
                        
                        time.sleep(0.5)
                    
                    except Exception as e:
                        print(f"  ⚠️ Pre-load {i+1}/3 failed")
                
                print("✅ Model locked in RAM!")
                print("💡 Will stay loaded for 30 minutes")
                print("⚡ Expected: 10-20 seconds per request (detailed feedback)")
            
            else:
                print("❌ Qwen 1.5B not found")
        
    except:
        print("⚠️ Could not pre-load (Ollama may not be running)")
    
    print("="*60)
    print("🎯 DevNest Ready!")
    print("="*60 + "\n")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("\n👋 DevNest shutting down\n")


# ============================================
# AUTHENTICATION ENDPOINTS
# ============================================

@app.post("/api/register")
async def register(request: Request, db: Session = Depends(get_db)):
    try:
        data = await request.json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            raise HTTPException(status_code=400, detail="Missing required fields")
        
        # Store original username for display
        display_name = username.strip()
        
        # Convert to lowercase for case-insensitive matching
        username_lower = username.lower().strip()
        email_lower = email.lower().strip()
        
        # Check if user exists (case-insensitive check)
        existing_user = db.query(User).filter(
            (User.username == username_lower) | (User.email == email_lower)
        ).first()
        
        if existing_user:
            raise HTTPException(status_code=400, detail="Username or email already exists")
        
        # Create new user with both lowercase and display name
        hashed_password = get_password_hash(password)
        new_user = User(
            username=username_lower,      # Lowercase for matching
            display_name=display_name,    # Original for display
            email=email_lower,            # Lowercase for matching
            hashed_password=hashed_password
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return {"message": "User created successfully", "username": display_name}
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"Registration error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        # Convert username to lowercase for case-insensitive matching
        username_lower = form_data.username.lower().strip()

        user = db.query(User).filter(User.username == username_lower).first()
        
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect username or password")
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, 
            expires_delta=access_token_expires
        )
        
        return {
            "access_token": access_token, 
            "token_type": "bearer", 
            "username": user.display_name  # Return display name (original capitalization)
        }
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"Login error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/history")
async def get_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    print(f"[DEBUG] GET /api/history called - ENDPOINT 2 - User: {current_user.username}")
    try:
        
        
        history = db.query(CodeHistory).filter(
            CodeHistory.user_id == current_user.id
        ).order_by(CodeHistory.created_at.desc()).limit(50).all()
        
        import json
        history_data = []
        for entry in history:
            history_data.append({
                'id': entry.id,
                'code': entry.code,
                'analysis_result': json.loads(entry.analysis_result) if entry.analysis_result else {},
                'created_at': entry.created_at.isoformat() + 'Z',
            })
        
        return {'username': current_user.username, 'history': history_data}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/history/{history_id}")
async def get_history_detail(history_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.username == current_user).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        entry = db.query(CodeHistory).filter(
            CodeHistory.id == history_id,
            CodeHistory.user_id == user.id
        ).first()
        
        if not entry:
            raise HTTPException(status_code=404, detail="History entry not found")
        
        import json
        return {
            'id': entry.id,
            'code': entry.code,
            'analysis_result': json.loads(entry.analysis_result) if entry.analysis_result else {},
            'feedback': json.loads(entry.ai_feedback) if entry.ai_feedback else [],
            'created_at': entry.created_at.isoformat() + 'Z',
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/history/{history_id}")
async def delete_history(history_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        
        entry = db.query(CodeHistory).filter(
            CodeHistory.id == history_id,
            CodeHistory.user_id == current_user.id
        ).first()
        
        if not entry:
            raise HTTPException(status_code=404, detail="History entry not found")
        
        db.delete(entry)
        db.commit()
        
        return {'message': 'History deleted successfully'}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # ============================================================================
# AI EXPLANATION HISTORY ENDPOINTS
# ============================================================================

@app.post("/api/ai-history")
async def save_ai_explanation(
    request: Request,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Save AI explanation to history"""
    try:
        data = await request.json()
        code = data.get("code", "")
        explanation = data.get("explanation", "")
        code_summary = data.get("code_summary", "")
        topics = data.get("topics", "")
        
        if not code or not explanation:
            raise HTTPException(status_code=400, detail="Code and explanation required")
        
        ai_entry = AIExplanation(
            user_id=current_user.id,
            code=code,
            explanation=explanation,
            code_summary=code_summary,
            topics=topics
        )
        
        db.add(ai_entry)
        db.commit()
        db.refresh(ai_entry)
        
        return {
            "success": True,
            "id": ai_entry.id,
            "message": "AI explanation saved to history"
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/ai-history")
async def get_ai_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all AI explanations for current user"""
    try:
        explanations = db.query(AIExplanation).filter(
            AIExplanation.user_id == current_user.id
        ).order_by(AIExplanation.created_at.desc()).all()
        
        return {
            "success": True,
            "history": [
                {
                    "id": exp.id,
                    "code": exp.code,
                    "explanation": exp.explanation,
                    "code_summary": exp.code_summary,
                    "topics": exp.topics,
                    "created_at": exp.created_at.isoformat()
                }
                for exp in explanations
            ]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/ai-history/{id}")
async def get_ai_explanation(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get specific AI explanation"""
    try:
        explanation = db.query(AIExplanation).filter(
            AIExplanation.id == id,
            AIExplanation.user_id == current_user.id
        ).first()
        
        if not explanation:
            raise HTTPException(status_code=404, detail="AI explanation not found")
        
        return {
            "success": True,
            "id": explanation.id,
            "code": explanation.code,
            "explanation": explanation.explanation,
            "code_summary": explanation.code_summary,
            "topics": explanation.topics,
            "created_at": explanation.created_at.isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/ai-history/clear-all")
async def clear_all_ai_explanations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Clear all AI explanations for current user"""
    try:
        print(f"[DEBUG] Clear all AI explanations - User: {current_user.username}")
        
        deleted = db.query(AIExplanation).filter(
            AIExplanation.user_id == current_user.id
        ).delete()
        
        db.commit()
        
        return {
            "success": True,
            "deleted_count": deleted,
            "message": f"Deleted {deleted} AI explanation(s)"
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    

@app.delete("/api/ai-history/{id}")
async def delete_ai_explanation(
    id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete specific AI explanation"""
    try:
        explanation = db.query(AIExplanation).filter(
            AIExplanation.id == id,
            AIExplanation.user_id == current_user.id
        ).first()
        
        if not explanation:
            raise HTTPException(status_code=404, detail="AI explanation not found")
        
        db.delete(explanation)
        db.commit()
        
        return {
            "success": True,
            "message": "AI explanation deleted successfully"
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/api/history/clear-all")
async def clear_all_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Clear all code analysis history for current user"""
    try:

        print(f"[DEBUG] Clear all history - User ID: {current_user.id}, Username: {current_user.username}")
       
        deleted = db.query(CodeHistory).filter(
            CodeHistory.user_id == current_user.id
        ).delete()
        
        db.commit()
        
        return {
            "success": True,
            "deleted_count": deleted,
            "message": f"Deleted {deleted} history entr{'y' if deleted == 1 else 'ies'}"
        }
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

