from datetime import datetime

"""
==========================================================
Decision Log Service
==========================================================

Purpose:
--------
Stores AI decision logs into the database.

Workflow:
--------
Receive Decision Data
        ↓
Connect Database
        ↓
Save Decision Log
        ↓
Return Decision ID

Author : Ajay Kichara
==========================================================
"""

from backend.database.database_connection import DatabaseConnection

class DecisionLogService:
    """
    Handles decision log database operations.
    """

    def __init__(self):
        """
        Initialize database connection.
        """

        self.database = DatabaseConnection()

    # ======================================================
    # Save Decision Log
    # ======================================================

    def save_decision_log(
        self,
        transaction_id: int,
        decision_result: dict
    ) -> int:
        """
        Saves the AI decision into the decision_logs table.

        Parameters
        ----------
        transaction_id : int
            Transaction ID from transactions table.

        decision_result : dict
            Dictionary containing the AI decision details.

        Returns
        -------
        int
            Generated decision_id.
        """

        connection = None
        cursor = None

        try:

            connection = self.database.connect()

            cursor = connection.cursor()

            query = """
            INSERT INTO decision_logs (

                transaction_id,
                model_prediction,
                model_confidence,
                confidence_zone,
                risk_score,
                risk_level,
                prediction_probability,
                model_version,
                frequency_last_24h,
                historical_success_rate,
                anomaly_score,
                final_decision,
                override_reason,
                decision_time)

            VALUES (

                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s

            )
            """

            values = (

                transaction_id,

                
                decision_result["model_prediction"],

                decision_result["confidence_score"],

                decision_result["confidence_zone"],

                decision_result["risk_score"],

                decision_result["risk_level"],

                decision_result["confidence_score"],

                "v1.0",

                decision_result["frequency_last_24h"],

                decision_result["historical_success_rate"],

                decision_result["anomaly_score"],

                decision_result["final_decision"],

                decision_result["override_reason"],

                datetime.now()

            )

            cursor.execute(query, values)

            connection.commit()

            decision_id = cursor.lastrowid

            return decision_id

        except Exception as e:

            print(f"❌ Error saving decision log: {e}")

            raise

        finally:

            if cursor is not None:
                cursor.close()

            if connection is not None:
                self.database.close(connection)

#

    # ======================================================
    # Get All Decision Logs
    # ======================================================

    def get_all_decision_logs(self):

        connection = None
        cursor = None

        try:

            connection = self.database.connect()

            cursor = connection.cursor(dictionary=True)

            query = """
            SELECT *
            FROM decision_logs
            ORDER BY decision_id DESC
            """

            cursor.execute(query)

            result = cursor.fetchall()

            return result

        except Exception as e:

            print(f"❌ Error fetching decision logs: {e}")

            raise

        finally:

            if cursor is not None:
                cursor.close()

            if connection is not None:
                self.database.close(connection)