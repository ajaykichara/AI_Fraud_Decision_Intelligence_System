"""
==========================================================
Prediction Engine
==========================================================

Purpose:
--------
Loads the trained Machine Learning model and predicts
whether a transaction is fraudulent.

Workflow:
Transaction
      ↓
Load Trained Model
      ↓
Predict Fraud
      ↓
Predict Probability
      ↓
Return Prediction Result

Dataset:
--------
Sparkov Credit Card Fraud Detection Dataset

Author : Ajay Kichara
==========================================================
"""

import joblib
import pandas as pd
from typing import Dict


class PredictionEngine:
    """
    Loads the trained model and performs fraud prediction.
    """

    def __init__(self):
        """
        Automatically loads the trained model
        when the object is created.
        """

        self.model = self.load_model()

    # ======================================================
    # Load Model
    # ======================================================

    def load_model(self):
        """
        Loads the trained Machine Learning pipeline.
        """

        try:

            model = joblib.load("models/fraud_detection_model.pkl")

            print("✅ Model loaded successfully.")

            return model

        except Exception as e:

            print(f"❌ Error loading model: {e}")

            raise

    # ======================================================
    # Predict Transaction
    # ======================================================

    def predict(self, transaction: Dict) -> Dict:
        """
        Predicts whether a transaction is fraud.

        Parameters
        ----------
        transaction : Dict
            Dictionary containing transaction details.

        Returns
        -------
        Dict
            Prediction result and fraud probability.
        """

        try:

            input_data = pd.DataFrame([transaction])
            prediction = int(
                     self.model.predict(input_data)[0]
            )

            probabilities = self.model.predict_proba(input_data)[0]

            probability = float(
                probabilities[prediction]
            )

            return {

                    "prediction": prediction,

                    "probability": round(probability, 4)

            }


        except Exception as e:

            print(f"❌ Prediction Error: {e}")

            raise