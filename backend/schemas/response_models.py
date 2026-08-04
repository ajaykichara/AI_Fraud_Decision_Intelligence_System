"""
==========================================================
Response Models
==========================================================

Purpose:
--------
Defines the API response models returned by FastAPI.

Author : Ajay Kichara
==========================================================
"""

from typing import Optional
from pydantic import BaseModel


class DecisionResponse(BaseModel):
    """
    Response model for fraud detection decision.
    """

    transaction_id: int

    decision_id: int

    model_prediction: int

    confidence_score: float

    confidence_zone: str

    risk_score: int

    risk_level: str

    final_decision: str

    override_reason: str

    review_id: Optional[int] = None  

