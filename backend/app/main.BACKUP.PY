from fastapi import FastAPI, HTTPException
OLLAMA_MODEL = "qwen2.5-coder:7b-instruct"
# Enabeling CORS (Cross-Origin Resource Sharing)
from fastapi.middleware.cors import CORSMiddleware
from app.models import CodeInput, AnalysisResponse, FeedbackItem, ComplexityMetrics
from app.analyzers.pylint_analyzer import PylintAnalyzer
from app.analyzers.radon_analyzer import RadonAnalyzer
from app.analyzers.rule_engine import RuleEngine

# REST API Initialization
app = FastAPI(title="DevNest API", version="1.0.0")

# Enable CORS - CRITICAL for frontend to connect!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
async def analyze_code(input_data: CodeInput):

    try:
        code = input_data.code  # Step 1: Extract the code
        
        if not code.strip(): # Step 2: Validate input
            raise HTTPException(status_code=400, detail="Code cannot be empty")
        
        # Step 3: Analyze complexity with Radon
        complexity_data = radon_analyzer.analyze(code)
        
        # Step 4: Detect issues with Pylint
        pylint_issues = pylint_analyzer.analyze(code)
        
        # Step 5: Translate issues using (Custom) Rule Engine
        # This is my contribution to the project :)
        
        feedback_items = [] # Create empty list to store final feedback
        
        for issue in pylint_issues:

            translated = rule_engine.translate_message(
                error_code=issue['code'],
                line=issue['line'],
                symbol=issue.get('symbol')
            )
            feedback_items.append(FeedbackItem(**translated))
        
        # Step 6: Add optimizations suggestions

        code_lines = code.split('\n')

        optimizations = rule_engine.add_optimization_suggestions(code_lines)
        for opt in optimizations:
            feedback_items.append(FeedbackItem(**opt))
        
        # Step 7: Return JSON response
        return AnalysisResponse(
            success=True,
            complexity=ComplexityMetrics(**complexity_data),
            feedback=feedback_items
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# ========================================
# AI EXPLANATION ENDPOINT
# ========================================

import requests
import time

# Ollama Configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "qwen2.5-coder:7b-instruct"

@app.post("/api/ai-explain")
async def ai_explain(input_data: CodeInput):
    """
    AI explains code using Qwen2.5-Coder 7B
    Optimized for consistent, student-friendly feedback
    """
    try:
        code = input_data.code
        
        if not code.strip():
            raise HTTPException(status_code=400, detail="Code cannot be empty")
        
        # OPTIMIZED PROMPT - Strict structure for consistency
        # OPTIMIZED SHORT PROMPT - Faster processing
        prompt = f"""<|im_start|>system
You are a Python teacher. Give brief, clear feedback.
<|im_end|>
<|im_start|>user
Analyze this code:
```python
{code}
```

Format (keep brief):

🎯 WHAT IT DOES: [1-2 sentences]

✅ GOOD: 
- [Point 1]
- [Point 2]

🔧 IMPROVE:
🔴 [Critical issue if any]: [Fix]
🟡 [Style issue if any]: [Fix]

💡 TIP: [One tip]

🎓 TAKEAWAY: [One sentence]

Be concise. Use "you/your". Under 250 words.
<|im_end|>
<|im_start|>assistant
"""

        print(f"\n{'='*60}")
        print("🤖 AI Analysis Request - Ollama Qwen2.5")
        print(f"{'='*60}")
        print(f"Code length: {len(code)} characters")
        print("Sending to Ollama...")
        
        start_time = time.time()
        
        # OPTIMIZED PAYLOAD - Better parameters for consistency
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                # Speed optimizations
                "temperature": 0.3,        # Faster, more consistent
                "top_p": 0.8,             # Focused responses
                "top_k": 20,              # Fewer choices = faster
                "num_predict": 500,       # Shorter responses = faster
                "num_ctx": 1024,          # Less context = faster
                "num_thread": 4,          # Use 4 CPU cores
                "num_batch": 512,         # Batch processing
                "repeat_penalty": 1.1,    # Prevent loops
                "repeat_last_n": 64,
                "stop": [
                    "<|im_end|>",
                    "```python",
                    "\n\n\n",
                    "USER:",
                    "STUDENT:"
                ],
                "numa": False,
                "num_keep": 4,
            },
            "keep_alive": "30m"  # CRITICAL: Keep loaded 30 minutes!
        }
        
        # Send request to Ollama
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=90  # Longer timeout for first request
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
        
        # Validate response quality
        if not ai_explanation:
            raise HTTPException(
                status_code=500,
                detail="AI returned empty response. Try again."
            )
        
        if len(ai_explanation) < 100:
            print(f"⚠️ Warning: Short response ({len(ai_explanation)} chars)")
            print(f"Response: {ai_explanation}")
        
        # Check if response follows format
        has_structure = (
            '🎯' in ai_explanation or 
            'WHAT YOUR CODE DOES' in ai_explanation.upper()
        )
        
        if not has_structure:
            print("⚠️ Warning: Response doesn't follow expected format")
            print(f"First 200 chars: {ai_explanation[:200]}")
        
        print(f"✅ AI Response Received")
        print(f"Response length: {len(ai_explanation)} characters")
        print(f"Has expected structure: {has_structure}")
        print(f"{'='*60}\n")
        
        return {
            "success": True,
            "explanation": ai_explanation,
            "model": "Qwen2.5-Coder 7B (Ollama)",
            "response_time": elapsed
        }
        
    except requests.exceptions.Timeout:
        print("⏰ Timeout: Request took too long")
        raise HTTPException(
            status_code=504,
            detail="AI response timeout (>90s). The model may be loading. Try again."
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
            
            has_qwen = any('qwen2.5-coder:7b' in name for name in model_names)
            
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
                    "expected_response_time": "3-5 seconds"
                }
            else:
                return {
                    "status": "model_not_found",
                    "ollama_running": True,
                    "model": OLLAMA_MODEL,
                    "model_available": False,
                    "message": f"❌ Model not found. Download it: ollama pull qwen2.5-coder:7b-instruct",
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
            
            has_qwen = any('qwen2.5-coder:7b' in name for name in model_names)
            
            if has_qwen:
                print(f"✅ Qwen 7B found")
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
                print("⚡ Expected: 5-10 seconds per request")
            
            else:
                print("❌ Qwen 7B not found")
        
    except:
        print("⚠️ Could not pre-load (Ollama may not be running)")
    
    print("="*60)
    print("🎯 DevNest Ready!")
    print("="*60 + "\n")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    print("\n👋 DevNest shutting down\n")   