from fastapi import FastAPI, HTTPException
from backend.schemas.request_models import TransactionRequest
from backend.services.transaction_service import TransactionService
from backend.schemas.response_models import DecisionResponse
from backend.services.decision_log_service import DecisionLogService
# ======================================================
# Create FastAPI Application
# ======================================================

app = FastAPI()

# ======================================================
# Create Transaction Service
# ======================================================

transaction_service = TransactionService()
# ======================================================
# Create Decision Log Service
# ======================================================
decision_log_service = DecisionLogService()

# ======================================================
# Home Route
# ======================================================

@app.get("/")
def home():

   return {
    "message": "Welcome to AI Fraud Decision Intelligence System (AFDIS)"
}

# ======================================================
# Fraud Detection API
# ======================================================

@app.post(
    "/decision/evaluate",
    response_model=DecisionResponse
)
def evaluate_transaction(transaction: TransactionRequest):

    try:

        transaction_dict = transaction.model_dump()

        result = transaction_service.process_transaction(transaction_dict)

        return result

    except Exception as e:

        print(f"❌ API Error: {e}")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
# ======================================================
# Decision History API
# ======================================================

@app.get("/decision/history")
def get_decision_history():

    try:

        history = decision_log_service.get_all_decision_logs()

        return history

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )