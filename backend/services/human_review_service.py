from datetime import datetime

"""
==========================================================
Human Review Service
==========================================================

Purpose:
--------
Stores transactions that require manual review.

Workflow:
--------
Receive Decision ID
        ↓
Connect Database
        ↓
Save Human Review
        ↓
Return Review ID

Author : Ajay Kichara
==========================================================
"""

from backend.database.database_connection import DatabaseConnection

class HumanReviewService:
    """
    Handles human review database operations.
    """

    def __init__(self):
        """
        Initialize database connection.
        """

        self.database = DatabaseConnection()

    # ======================================================
    # Save Human Review
    # ======================================================

    def save_human_review(
        self,
        decision_id: int
    ) -> int:
        """
        Saves a manual review request into the human_review table.

        Parameters
        ----------
        decision_id : int
            Decision ID from decision_logs table.

        Returns
        -------
        int
            Generated review_id.
        """

        connection = None
        cursor = None

        try:

            connection = self.database.connect()

            cursor = connection.cursor()

            query = """
            INSERT INTO human_review (

                decision_id,
                reviewer_name,
                review_status,
                review_comment,
                review_time

            )

            VALUES (

                %s,
                %s,
                %s,
                %s,
                %s

            )
            """

            values = (

                decision_id,

                None,

                "PENDING",

                None,

                datetime.now()

            )

            cursor.execute(query, values)

            connection.commit()

            review_id = cursor.lastrowid

            return review_id

        except Exception as e:

            print(f"❌ Error saving human review: {e}")

            raise

        finally:

            if cursor is not None:
                cursor.close()

            if connection is not None:
                self.database.close(connection)