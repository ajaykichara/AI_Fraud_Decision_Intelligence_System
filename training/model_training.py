
import pandas as pd

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("data/final_credit_fraud_dataset.csv")

# ==========================
# Libraries
# ==========================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

from xgboost import XGBClassifier
from imblearn.over_sampling import RandomOverSampler

# ==========================
# Features & Target
# ==========================
X = df.drop(columns=["is_fraud"])
y = df["is_fraud"]

# ==========================
# Train Test Split
# ==========================
x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# ==========================
# Apply Oversampling
# ==========================
# This duplicates the minority class (1) to match the massive majority class (0)
ros = RandomOverSampler(random_state=42)
x_train_resampled, y_train_resampled = ros.fit_resample(x_train, y_train)

print("=" * 50)
print(f"Training data before oversampling:\n{y_train.value_counts()}")
print("-" * 50)
print(f"Training data after oversampling:\n{y_train_resampled.value_counts()}")
print("=" * 50)

# ==========================
# Categorical Columns
# ==========================
cat_columns = x_train_resampled.select_dtypes(
    include=["object", "category", "string"]
).columns.tolist()

# ==========================
# Preprocessing
# ==========================
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(
                drop="first",
                handle_unknown="ignore"
            ),
            cat_columns
        )
    ],
    remainder="passthrough"
)

# ==========================
# XGBoost Pipeline
# ==========================
pipeline = Pipeline([

    ("preprocessor", preprocessor),

    ("model", XGBClassifier(


        n_estimators=200,
        max_depth=12,
        
        random_state=42,
        n_jobs=-1

    ))
])

# ==========================
# Train
# ==========================
print("Training on oversampled data (this may take a few minutes)...")
pipeline.fit(x_train_resampled, y_train_resampled)

# ==========================
# Predict
# ==========================
y_pred = pipeline.predict(x_test)
y_prob = pipeline.predict_proba(x_test)[:, 1]

# ==========================
# Evaluation
# ==========================
print("=" * 50)
print("Accuracy :", accuracy_score(y_test, y_pred))
print("=" * 50)

print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))

print()

print("Classification Report")
print(classification_report(y_test, y_pred))

print()

print("ROC-AUC :", roc_auc_score(y_test, y_prob))

# ==========================
# Training Accuracy
# ==========================
# Checking accuracy on the resampled training data
train_pred = pipeline.predict(x_train_resampled)

print("=" * 50)
print("Training Accuracy :", accuracy_score(y_train_resampled, train_pred))
print("Testing Accuracy  :", accuracy_score(y_test, y_pred))
print("=" * 50)

# ==========================
# Save Model
# ==========================
import joblib

# joblib.dump(pipeline, "models/fraud_detection_model.pkl")

print("Model saved successfully!")


# model scave  this   data  
# ==================================================
# Training data before oversampling:
# is_fraud
# 0    1031335
# 1       6005
# Name: count, dtype: int64
# --------------------------------------------------
# Training data after oversampling:
# is_fraud
# 0    1031335
# 1    1031335
# Name: count, dtype: int64
# ==================================================
# Training on oversampled data (this may take a few minutes)...
# ==================================================
# Accuracy : 0.9982879287408178
# ==================================================
# Confusion Matrix
# [[257502    332]
#  [   112   1389]]

# Classification Report
#               precision    recall  f1-score   support

#            0       1.00      1.00      1.00    257834
#            1       0.81      0.93      0.86      1501

#     accuracy                           1.00    259335
#    macro avg       0.90      0.96      0.93    259335
# weighted avg       1.00      1.00      1.00    259335


# ROC-AUC : 0.9986283336364358
# ==================================================
# Training Accuracy : 0.9997658374824863
# Testing Accuracy  : 0.9982879287408178
# ==================================================
# Model saved successfully!
# (project _ml_1) PS C:\Users\HP\Downloads\projects\project _ml_1> 
# model detail  