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

        print(f"\n{'='*60}")
        print(f"📝 ANALYZING CODE")
        print(f"{'='*60}")

        # Analyze complexity with Radon
        complexity_data = radon_analyzer.analyze(code)
        print(f"✅ Radon analysis complete")

        # Detect issues with Pylint
        pylint_issues = pylint_analyzer.analyze(code)
        print(f"✅ Pylint found {len(pylint_issues)} issues")

        # DEBUG: Print what Pylint found
        for issue in pylint_issues:
            print(f"  DEBUG - Issue: {issue}")

        # Translate issues using Rule Engine
        feedback_items = []

        for issue in pylint_issues:
            print(f"\n Processing issue: {issue}")

            try:
                translated = rule_engine.translate_message(
                    error_code=issue['code'],
                    line=issue['line'],
                    symbol=issue.get('symbol')
                )

                print(f"Translated result type: {type(translated)}")
                print(f"Translated result: {translated}")

                if translated:
                    feedback_items.append(translated)
                    print(f"✅ Added (total: {len(feedback_items)})")
                else:
                    print(f"❌ translate_message returned None!")

            except Exception as e:
                print(f"❌ ERROR: {e}")
                import traceback
                traceback.print_exc()

        print(f"\n--- Translated {len(feedback_items)} issues")

        # Add optimizations suggestions
        code_lines = code.split('\n')

        try:
            optimizations = rule_engine.add_optimization_suggestions(code_lines)
            print(f"✅ Found {len(optimizations)} optimization suggestions")

            for opt in optimizations:
                # Build formatted message from optimization structure
                formatted_message = f"{opt.get('title', 'Optimization')}\n"
                formatted_message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
                formatted_message += f"📋 EXPLAIN:\n{opt.get('explain', '')}\n\n"
                formatted_message += f"🔧 HOW TO FIX:\n{opt.get('how_to_fix', '')}\n\n"
                formatted_message += "📝 EXAMPLE:\n\n"
                formatted_message += f"❌ WRONG:\n{opt.get('wrong', '')}\n\n"
                formatted_message += f"✅ RIGHT:\n{opt.get('right', '')}\n\n"
                formatted_message += f"📚 LEARN:\n{opt.get('learn', '')}"
