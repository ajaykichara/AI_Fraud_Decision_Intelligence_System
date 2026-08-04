"""
==========================================================
Transaction Service
==========================================================

Purpose:
--------
Coordinates the complete fraud detection workflow.

Workflow:
--------
Transaction
      ↓
Prediction Engine
      ↓
Decision Engine
      ↓
Save Transaction
      ↓
Save Decision Log
      ↓
Return Result

Author : Ajay Kichara
==========================================================
"""

from typing import Dict
from datetime import datetime

from backend.services.prediction_engine import PredictionEngine
from backend.services.decision_engine import DecisionEngine
from backend.database.database_connection import DatabaseConnection
from backend.services.decision_log_service import DecisionLogService
from backend.services.human_review_service import HumanReviewService


class TransactionService:
    """
    Handles the complete transaction processing workflow.
    """

    def __init__(self):
        """
        Initialize all required services.
        """

        self.prediction_engine = PredictionEngine()

        self.decision_engine = DecisionEngine()

        self.database = DatabaseConnection()
        self.decision_log_service = DecisionLogService()
        self.human_review_service = HumanReviewService()


    # ======================================================
    # Process Transaction
    # ======================================================

    def process_transaction(self, transaction: Dict) -> Dict:
                """
                Processes a complete transaction.

                Workflow:
                Transaction
                    ↓
                Prediction Engine
                    ↓
                Decision Engine
                    ↓
                Return Final Result
                """
                try:
                        # ------------------------------------------
                        # Machine Learning Prediction
                        # ------------------------------------------

                        prediction_result = self.prediction_engine.predict(transaction)

                        model_prediction = prediction_result["prediction"]

                        probability = prediction_result["probability"]

                        # ------------------------------------------
                        # Business Decision
                        # ------------------------------------------

                        decision_result = self.decision_engine.make_decision(

                            model_prediction=model_prediction,

                            probability=probability,

                            transaction_amount=transaction["transaction_amount"],

                            is_night_transaction=transaction["is_night_transaction"],

                            high_amount_transaction=transaction["high_amount_transaction"]

                        )



                        transaction_id = self.save_transaction(transaction,model_prediction) 

                        # Calculate frequency
                        frequency_last_24h = self.calculate_frequency_last_24h(transaction)

                        # Store it in decision_result
                        decision_result["frequency_last_24h"] = frequency_last_24h

                        # Calculate historical success rate
                        historical_success_rate = self.calculate_historical_success_rate(transaction)

                        # Store it in decision_result
                        decision_result["historical_success_rate"] = historical_success_rate

                        # Calculate anomaly score
                        anomaly_score = self.calculate_anomaly_score(transaction)

                        # Store it in decision_result
                        decision_result["anomaly_score"] = anomaly_score


                        decision_id = self.decision_log_service.save_decision_log(transaction_id,
                        decision_result)
                        if decision_result["final_decision"] == "MANUAL_REVIEW":

                            review_id = self.human_review_service.save_human_review(decision_id)
                            decision_result["review_id"] = review_id

                        decision_result["transaction_id"] = transaction_id
                        decision_result["decision_id"] = decision_id

                        return decision_result
                except Exception as e:

                     print(f"❌ Transaction Processing Error: {e}")

                     raise
    # ======================================================
    # Calculate Frequency (24 Hours)
    # ======================================================
    def calculate_frequency_last_24h(self, transaction: Dict) -> int:

        connection = None
        cursor = None

        try:

            connection = self.database.connect()
            cursor = connection.cursor()

            query = """
            SELECT COUNT(*)
            FROM transactions
            WHERE customer_zip = %s
            AND transaction_time >= NOW() - INTERVAL 24 HOUR
            """

            cursor.execute(query, (transaction["customer_zip"],))

            result = cursor.fetchone()

            return result[0]

        except Exception as e:

            print(f"❌ Error calculating frequency: {e}")
            raise

        finally:

            if cursor is not None:
                cursor.close()

            if connection is not None:
                self.database.close(connection)
    # ======================================================
    # Calculate Historical Success Rate
    # ======================================================

    def calculate_historical_success_rate(self, transaction: Dict) -> float:
        """
        Calculates the customer's historical transaction success rate.

        Success Rate =
        Number of APPROVED transactions
        --------------------------------
        Total previous transactions

        This value is later stored in the decision_logs table
        for business analysis and auditing.
        """

        connection = None
        cursor = None

        try:

            connection = self.database.connect()
            cursor = connection.cursor()

            query = """
            SELECT
                COUNT(*) AS total_transactions,

                SUM(
                    CASE
                        WHEN dl.final_decision = 'APPROVE'
                        THEN 1
                        ELSE 0
                    END
                ) AS approved_transactions

            FROM transactions t

            INNER JOIN decision_logs dl
                ON t.transaction_id = dl.transaction_id

            WHERE t.customer_zip = %s
            """

            cursor.execute(query, (transaction["customer_zip"],))

            result = cursor.fetchone()

            total_transactions = result[0]
            approved_transactions = result[1] or 0

            if total_transactions == 0:
                return 0.0

            success_rate = approved_transactions / total_transactions

            return round(success_rate, 2)

        except Exception as e:

            print(f"❌ Error calculating historical success rate: {e}")
            raise

        finally:

            if cursor is not None:
                cursor.close()

            if connection is not None:
                self.database.close(connection)
    # ======================================================
    # Calculate Anomaly Score
    # ======================================================

    def calculate_anomaly_score(self, transaction: Dict) -> float:
        """
        Calculates an anomaly score using business rules.

        Returns
        -------
        float
            Anomaly score between 0.0 and 1.0
        """

        score = 0.0

        # High amount transaction
        if transaction["transaction_amount"] >= 550:
            score += 0.5

        # Night transaction
        if transaction["is_night_transaction"]:
            score += 0.2

        # Feature engineered flag
        if transaction["high_amount_transaction"]:
            score += 0.3

        return round(min(score, 1.0), 2)  

    # ======================================================
    # Save Transaction
    # ======================================================

    def save_transaction(self, transaction: Dict,model_prediction: int) -> int:
        """
        Saves the transaction into the database.

        Returns
        -------
        int
            Generated transaction_id
        
        """
        connection = None
        cursor = None

        try:

            connection = self.database.connect()

            cursor = connection.cursor()


            query = """
            INSERT INTO transactions (
                transaction_time,
                merchant,
                merchant_category,
                transaction_amount,
                gender,
                city,
                state,
                customer_zip,
                city_population,
                job,
                merchant_zip,
                customer_age,
                transaction_hour,
                transaction_day,
                transaction_month,
                transaction_weekday,
                is_weekend,
                is_night_transaction,
                high_amount_transaction,
                population_group,
                age_group,
                merchant_distance,
                is_fraud

            )

            VALUES (

                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s

            )
            """

            values = (
                datetime.now(),
                transaction["merchant"],
                transaction["merchant_category"],
                transaction["transaction_amount"],
                transaction["gender"],
                transaction["city"],
                transaction["state"],
                transaction["customer_zip"],
                transaction["city_population"],
                transaction["job"],
                transaction["merchant_zip"],
                transaction["customer_age"],
                transaction["transaction_hour"],
                transaction["transaction_day"],
                transaction["transaction_month"],
                transaction["transaction_weekday"],
                transaction["is_weekend"],
                transaction["is_night_transaction"],
                transaction["high_amount_transaction"],

                None,   # population_group
                None,   # age_group
                None,   # merchant_distance

                model_prediction    # is_fraud (updated later)

            )

            cursor.execute(query, values)

            connection.commit()

            transaction_id = cursor.lastrowid

            return transaction_id
        
        except Exception as e:

            print(f"❌ Error saving transaction: {e}")

            raise

        finally:

            if cursor is not None:
                cursor.close()

            if connection:
               self.database.close(connection)

