"""
==========================================================
Decision Control Engine
==========================================================

Purpose:
--------
Applies business rules after the ML model prediction.

Workflow:
Transaction
      ↓
xgboost classifier Prediction
      ↓
Decision Engine
      ↓
APPROVE / REJECT / MANUAL_REVIEW

Dataset:
--------
Sparkov Credit Card Fraud Detection Dataset
Currency : USD

Author : Ajay Kichara
==========================================================
"""

from typing import Dict


class DecisionEngine:

    def __init__(self):

        # ======================================================
        # Confidence Thresholds
        # ======================================================

        self.HIGH_CONFIDENCE = 0.80
        self.MEDIUM_CONFIDENCE = 0.55

        # ======================================================
        # Amount Thresholds
        #
        # Derived from dataset statistics
        #
        # 95th Percentile ≈ $196
        # 99th Percentile ≈ $546
        # ======================================================

        self.MEDIUM_AMOUNT = 200
        self.HIGH_AMOUNT = 550

    # ==========================================================
    # Confidence Zone
    # ==========================================================

    def get_confidence_zone(self, probability: float) -> str:
        """
        Returns confidence zone.

        HIGH
        MEDIUM
        LOW
        """

        if probability >= self.HIGH_CONFIDENCE:
            return "HIGH"

        elif probability >= self.MEDIUM_CONFIDENCE:
            return "MEDIUM"

        return "LOW"

    # ==========================================================
    # Risk Score
    # ==========================================================

    def calculate_risk_score(
        self,
        transaction_amount: float,
        is_night_transaction: bool,
        high_amount_transaction: bool
    ) -> int:
        """
        Calculates overall transaction risk score.
        """

        score = 0

        # ----------------------------------------
        # Amount Risk
        # ----------------------------------------

        if transaction_amount >= self.HIGH_AMOUNT:

            score += 3

        elif transaction_amount >= self.MEDIUM_AMOUNT:

            score += 2

        # ----------------------------------------
        # Night Transaction
        # ----------------------------------------

        if is_night_transaction:

            score += 1

        # ----------------------------------------
        # Feature Engineered Flag
        # ----------------------------------------

        if high_amount_transaction:

            score += 2

        return score

    # ==========================================================
    # Risk Level
    # ==========================================================

    def get_risk_level(self, score: int) -> str:
        """
        Converts score into a business risk level.
        """

        if score >= 5:

            return "HIGH"

        elif score >= 2:

            return "MEDIUM"

        return "LOW"

    # ==========================================================
    # Final Decision
    # ==========================================================

    def make_decision(
        self,
        model_prediction: int,
        probability: float,
        transaction_amount: float,
        is_night_transaction: bool,
        high_amount_transaction: bool
    ) -> Dict:

        confidence_zone = self.get_confidence_zone(probability)

        risk_score = self.calculate_risk_score(
            transaction_amount,
            is_night_transaction,
            high_amount_transaction
        )

        risk_level = self.get_risk_level(risk_score)

        # ======================================================
        # Genuine Transaction
        # ======================================================

        if model_prediction == 0:

            if confidence_zone == "HIGH":

                final_decision = "APPROVE"
                reason = "Model is highly confident that the transaction is genuine."

            elif confidence_zone == "MEDIUM":

                final_decision = "APPROVE"
                reason = "Transaction appears genuine with moderate confidence."

            else:

                final_decision = "MANUAL_REVIEW"
                reason = "Low confidence genuine prediction. Manual verification recommended."

        # ======================================================
        # Fraud Transaction
        # ======================================================

        else:

            if confidence_zone == "HIGH" and risk_level == "HIGH":

                final_decision = "REJECT"
                reason = "High confidence fraud prediction with high business risk."

            elif confidence_zone == "HIGH" and risk_level == "MEDIUM":

                final_decision = "MANUAL_REVIEW"
                reason = "Fraud predicted with high confidence but medium business risk."

            elif confidence_zone == "MEDIUM":

                final_decision = "MANUAL_REVIEW"
                reason = "Fraud prediction requires analyst verification."

            else:

                final_decision = "MANUAL_REVIEW"
                reason = "Low confidence fraud prediction."

        return {
            "model_prediction": int(model_prediction),
            "confidence_score": round(probability, 4),
            "confidence_zone": confidence_zone,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "final_decision": final_decision,
            "override_reason": reason
        }