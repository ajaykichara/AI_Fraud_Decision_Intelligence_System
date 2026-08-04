"""
==========================================================
Request Models
==========================================================

Purpose:
--------
Defines the API request models received by FastAPI.

Author : Ajay Kichara
==========================================================
"""

from pydantic import BaseModel, Field


# ======================================================
# Request Model
# ======================================================

class TransactionRequest(BaseModel):
    """
    Request model for transaction evaluation.
    """

    merchant: str = Field(
        ...,
        min_length=1,
        max_length=150,
        description="Merchant name."
    )

    merchant_category: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Merchant category."
    )

    transaction_amount: float = Field(
        ...,
        gt=0,
        description="Transaction amount must be greater than 0."
    )

    gender: str = Field(
        ...,
        min_length=1,
        max_length=10,
        description="Customer gender."
    )

    city: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Customer city."
    )

    state: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Customer state."
    )

    customer_zip: int = Field(
        ...,
        gt=0,
        description="Customer ZIP code."
    )

    city_population: int = Field(
        ...,
        gt=0,
        description="City population must be greater than 0."
    )

    job: str = Field(
        ...,
        min_length=1,
        max_length=150,
        description="Customer occupation."
    )

    merchant_zip: int = Field(
        ...,
        gt=0,
        description="Merchant ZIP code."
    )

    customer_age: int = Field(
        ...,
        ge=18,
        le=120,
        description="Customer age must be between 18 and 120."
    )

    transaction_hour: int = Field(
        ...,
        ge=0,
        le=23,
        description="Transaction hour (0-23)."
    )

    transaction_day: int = Field(
        ...,
        ge=1,
        le=31,
        description="Transaction day (1-31)."
    )

    transaction_month: int = Field(
        ...,
        ge=1,
        le=12,
        description="Transaction month (1-12)."
    )

    transaction_weekday: int = Field(
        ...,
        ge=0,
        le=6,
        description="Transaction weekday (0-6)."
    )

    is_weekend: bool

    is_night_transaction: bool

    high_amount_transaction: bool