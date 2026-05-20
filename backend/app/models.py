from pydantic import BaseModel
from typing import List, Optional

# Requist models for API input and output (Recive)
class CodeInput(BaseModel):
    code: str

# Resonse models for analysis results (Return)
class FeedbackItem(BaseModel):
    type: str
    line: int
    message: str
    code: str
    severity: Optional[str] = None
    structured: Optional[dict] = None

class ComplexityMetrics(BaseModel):
    score: str
    cyclomatic: float
    maintainability: float

class AnalysisResponse(BaseModel):
    success: bool
    complexity: ComplexityMetrics
    feedback: List[FeedbackItem]

    # Data Validation and Serialization handled by Pydantic