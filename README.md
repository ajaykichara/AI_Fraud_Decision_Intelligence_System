# 🛡️ AI Fraud Decision Intelligence System (AFDIS)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green?logo=fastapi)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![License](https://img.shields.io/badge/License-Educational-green)


> **An end-to-end Machine Learning Inference System that combines XGBoost, FastAPI, MySQL, and Streamlit with a rule-based Decision Engine to deliver intelligent, risk-aware, and auditable fraud decisions.**

---

# 📌 Executive Summary

Financial fraud detection requires more than accurate machine learning predictions. In real-world environments, organizations must evaluate prediction confidence, business risk, historical behavior, and operational policies before taking action.

The **AI Fraud Decision Intelligence System (AFDIS)** extends traditional fraud classification by integrating a machine learning inference pipeline with a rule-based Decision Engine, enabling business-aware fraud decisions instead of relying solely on raw model predictions.

The platform combines an **XGBoost classification model**, a **FastAPI REST API**, a **MySQL persistence layer**, and a **Streamlit operational dashboard** into a modular decision support system capable of evaluating transactions, applying configurable business rules, maintaining an audit trail, and supporting manual review workflows.

---

# 📖 Overview

The AI Fraud Decision Intelligence System is designed to demonstrate how machine learning models can be integrated into a production-style application architecture.

Instead of returning only a fraud prediction, the system performs multiple stages of decision processing, including:

- Machine Learning Inference
- Confidence Evaluation
- Risk Assessment
- Business Rule Evaluation
- Decision Logging
- Human Review Routing
- REST API Response
- Dashboard Visualization

This layered architecture transforms raw machine learning outputs into transparent and traceable business decisions.

---

# ✨ Key Features

- End-to-End Machine Learning Pipeline
- Feature Engineering Pipeline
- Data Preprocessing
- XGBoost Classification Model
- Fraud Probability Estimation
- Prediction Engine
- Decision Intelligence Layer
- Rule-Based Decision Engine
- Confidence Calibration
- Risk Assessment
- Business Intelligence Metrics
- Human-in-the-Loop Review Workflow
- FastAPI REST APIs
- MySQL Persistence
- Decision Audit Logging
- Transaction History
- Streamlit Operational Dashboard
- Interactive Analytics Dashboard
- Modular Service-Oriented Architecture
- Object-Oriented Design

---

# 🛠️ Technology Stack

## Programming Language

- Python

---

## Machine Learning

- XGBoost
- Scikit-learn
- imbalanced-learn

---

## Data Processing

- Pandas
- NumPy

---

## Backend Framework

- FastAPI
- Uvicorn
- Pydantic

---

## Database

- MySQL

---

## Dashboard & Visualization

- Streamlit
- Plotly

---

## Development Tools

- Git
- GitHub
- VS Code
- Jupyter Notebook

---

# 📂 Dataset

The project is built using a credit card fraud detection dataset containing customer information, merchant details, transaction attributes, and engineered features for binary fraud classification.

### Dataset Characteristics

- Binary Classification Problem
- Highly Imbalanced Dataset
- Customer Information
- Merchant Information
- Transaction Information
- Engineered Features
- Fraud Labels

The dataset is transformed into a feature-rich machine learning dataset before model training and real-time inference.

---

# 🏗️ High-Level System Architecture

```text
                   Client Application
                           │
                           ▼
                  FastAPI REST API
                           │
                           ▼
                 Prediction Engine
                           │
                           ▼
             XGBoost Classification Model
                           │
                           ▼
            Decision Intelligence Layer
                           │
                           ▼
             Business Rule Engine
                           │
                           ▼
                  MySQL Database
                           │
                           ▼
             Streamlit Dashboard
```

---

# 🔄 End-to-End Project Workflow

```text
                                  Raw Credit Card Dataset
                                           │
                                           ▼
                                data_preprocessing.py
                                           │
          ┌──────────────────────────────────────────────────────┐
          │ Data Preprocessing & Feature Engineering             │
          │ • Rename Columns                                     │
          │ • Handle Missing Values                              │
          │ • Customer Age                                       │
          │ • Transaction Hour / Day / Month / Weekday           │
          │ • Weekend Transaction                                │
          │ • Night Transaction                                  │
          │ • High Amount Transaction                            │
          └──────────────────────────────────────────────────────┘
                                           │
                                           ▼
                           final_credit_fraud_dataset.csv
                                           │
                                           ▼
                                 model_training.py
                                           │
          ┌──────────────────────────────────────────────────────┐
          │ Machine Learning Pipeline                            │
          │ • Train-Test Split                                   │
          │ • RandomOverSampler                                  │
          │ • OneHotEncoder                                      │
          │ • ColumnTransformer                                  │
          │ • Scikit-learn Pipeline                              │
          │ • XGBoost Training                                   │
          │ • Model Evaluation                                   │
          │ • Model Serialization (Joblib)                       │
          └──────────────────────────────────────────────────────┘
                                           │
                                           ▼
                           fraud_detection_model.pkl

══════════════════════ MODEL SERVING & APPLICATION LAYER ══════════════════════

                             Streamlit Dashboard
                              (app_streamlit.py)

        ┌────────────────────────────────────────────────────────────┐
        │ • Dashboard                                                │
        │ • Evaluate Transaction                                     │
        │ • Decision History                                         │
        │ • Analytics                                                │
        └────────────────────────────────────────────────────────────┘
                                           │
                                   HTTP REST API
                                           │
                                           ▼
                          FastAPI Application (main.py)
                                           │
                     ┌─────────────────────┴─────────────────────┐
                     │                                           │
                     ▼                                           ▼
          GET /decision/history                  POST /decision/evaluate
                     │                                           │
                     └─────────────────────┬─────────────────────┘
                                           │
                                           ▼
                    Request Schema (TransactionRequest)
                           request_models.py
                                           │
                                           ▼
                              TransactionService
                         (Workflow Orchestrator)
                                           │
              ┌────────────────────────────┼────────────────────────────┐
              │                            │                            │
              ▼                            ▼                            ▼
      PredictionEngine          Decision Intelligence Layer     Persistence Layer
 (Loads Serialized Model)        (Business Rule Engine)        (MySQL Connection)
              │                            │                            │
              └────────────────────────────┼────────────────────────────┘
                                           │
                                           ▼
                              Transaction Processing
                                           │
                 ┌─────────────────────────┼────────────────────────┐
                 │                         │                        │
                 ▼                         ▼                        ▼
      Transaction Persistence   Business Intelligence      Final Decision
                                 Metrics                   APPROVE
                                 • Frequency               REJECT
                                 • Historical Success      MANUAL REVIEW
                                 • Anomaly Score
                                           │
                                           ▼
                                DecisionLogService
                                           │
                                           ▼
                               HumanReviewService
                               (If MANUAL_REVIEW)
                                           │
                                           ▼
                                   MySQL Database
                             decision_control_system
                                           │
          ┌────────────────────────────────┼──────────────────────────────┐
          ▼                                ▼                              ▼
    transactions                    decision_logs                  human_review
                                           │
                                           ▼
                    Response Schema (DecisionResponse)
                           response_models.py
                                           │
                                           ▼
                              REST API JSON Response
                                           │
                                           ▼
                          Streamlit Dashboard Updates
```

---

# 📈 Project Highlights

- End-to-End Machine Learning Inference Pipeline
- Rule-Based Decision Intelligence
- Confidence-Based Decision Making
- Risk Assessment Engine
- Modular Backend Architecture
- RESTful API Integration
- Persistent Audit Logging
- Human Review Workflow
- Interactive Operational Dashboard
- Object-Oriented Service Layer

---

# ⚙️ Machine Learning Pipeline

The machine learning pipeline transforms raw transaction data into intelligent fraud decisions through a structured preprocessing, training, inference, and business decision workflow.

## 1. Data Preprocessing

The preprocessing stage prepares the raw transaction dataset for machine learning.

### Operations Performed

- Column Renaming
- Missing Value Handling
- Customer Age Calculation
- Transaction Date Feature Extraction
- Weekend Transaction Feature
- Night Transaction Feature
- High Amount Transaction Feature

The processed dataset is stored as:

```text
final_credit_fraud_dataset.csv
```

---

## 2. Feature Engineering

Additional features are engineered to improve predictive performance.

### Engineered Features

| Feature | Purpose |
|---------|---------|
| customer_age | Customer age derived from date of birth |
| transaction_hour | Hour of transaction |
| transaction_day | Day of month |
| transaction_month | Transaction month |
| transaction_weekday | Weekday of transaction |
| is_weekend | Weekend indicator |
| is_night_transaction | Night transaction indicator |
| high_amount_transaction | High-value transaction flag |

---

## 3. Data Preparation

The training pipeline performs:

- Train-Test Split
- Minority Class Oversampling using RandomOverSampler
- One-Hot Encoding of categorical variables
- Column-wise preprocessing using ColumnTransformer
- Unified preprocessing and training using a Scikit-learn Pipeline

---

## 4. Model Training

The fraud detection model is trained using:

- XGBoost Classifier

The trained model is serialized using Joblib and saved as:

```text
models/fraud_detection_model.pkl
```

---

## 5. Model Evaluation

The training script evaluates the model using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

---

## 6. Real-Time Inference

During prediction:

1. Transaction data is received by the FastAPI API.
2. PredictionEngine loads the serialized model.
3. Fraud probability is calculated.
4. Prediction results are forwarded to the Decision Engine.

---

## 7. Decision Intelligence

Instead of returning raw predictions, the system evaluates:

- Prediction Confidence
- Confidence Zone
- Transaction Risk Score
- Business Rules

The final business decision is:

- APPROVE
- REJECT
- MANUAL_REVIEW

---

# 📁 Project Structure

```text
AI_Fraud_Decision_Intelligence_System/
│
├── backend/
│   │
│   ├── database/
│   │   └── database_connection.py
│   │
│   ├── schemas/
│   │   ├── request_models.py
│   │   └── response_models.py
│   │
│   ├── services/
│   │   ├── prediction_engine.py
│   │   ├── decision_engine.py
│   │   ├── transaction_service.py
│   │   ├── decision_log_service.py
│   │   └── human_review_service.py
│   │
│   └── main.py
│
├── dashboard/
│   └── app_streamlit.py
│
├── data/
│
├── models/
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

# 📡 REST API Documentation

## GET /

Returns the API status message.

### Purpose

Checks whether the FastAPI application is running.

---

## POST /decision/evaluate

Evaluates a transaction and returns the fraud decision.

### Request

Receives a validated transaction using the TransactionRequest schema.

### Processing Flow

```
Transaction
      ↓
Prediction Engine
      ↓
Decision Engine
      ↓
Database Persistence
      ↓
Decision Logging
      ↓
Human Review (If Required)
      ↓
Response
```

### Response

Returns:

- Transaction ID
- Decision ID
- Model Prediction
- Confidence Score
- Confidence Zone
- Risk Score
- Risk Level
- Final Decision
- Decision Explanation
- Review ID (when applicable)

---

## GET /decision/history

Returns the stored decision history.

### Purpose

Provides historical fraud decisions for analytics and dashboard visualization.

---

# 🗄️ Database Design

The application stores operational data in the **decision_control_system** MySQL database.

## transactions

Stores transaction details submitted to the system.

### Contains

- Customer Information
- Merchant Information
- Transaction Features
- Engineered Features
- Model Prediction

---

## decision_logs

Stores every fraud decision generated by the Decision Engine.

### Contains

- Model Prediction
- Confidence Score
- Confidence Zone
- Risk Score
- Risk Level
- Historical Success Rate
- Frequency (24 Hours)
- Anomaly Score
- Final Decision
- Decision Time

---

## human_review

Stores transactions requiring manual verification.

### Contains

- Decision ID
- Review Status
- Reviewer Name
- Review Comment
- Review Time

---

# 🔄 End-to-End Project Workflow

```
Transaction
      ↓
FastAPI API
      ↓
Request Validation
      ↓
Prediction Engine
      ↓
Fraud Probability
      ↓
Decision Intelligence Layer
      ↓
Business Metrics
      ↓
Final Decision
      ↓
Store Transaction
      ↓
Store Decision Log
      ↓
Create Human Review (If Required)
      ↓
Return API Response
      ↓
Dashboard Update
```

---

# 📊 Dashboard Modules

The Streamlit dashboard contains four operational modules.

## 🏠 Dashboard

Displays:

- Total Transactions
- Approval Rate
- Decision Summary
- System Status

---

## 💳 Evaluate Transaction

Allows users to:

- Enter transaction details
- Submit transactions
- View prediction results
- Review confidence scores
- View decision explanations

---

## 📊 Decision History

Displays:

- Decision Logs
- Confidence Statistics
- Risk Metrics
- CSV Export

---

## 📈 Analytics

Provides:

- Decision Distribution
- Risk Distribution
- Confidence Distribution
- Risk Score Distribution

---

# 🏗️ Design Patterns Used

The project follows several software engineering practices.

### Layered Architecture

Separates API, business logic, persistence, and presentation.

### Service Layer

Business operations are organized into dedicated services.

### Pipeline Pattern

Machine learning preprocessing and model training are encapsulated in a Scikit-learn Pipeline.

### Object-Oriented Design

Responsibilities are divided across reusable classes.

### Modular Architecture

Each module has a single, well-defined responsibility, making the system easier to maintain and extend.

---

# 🤖 AI Concepts Demonstrated

- Binary Classification
- Feature Engineering
- Data Preprocessing
- Class Imbalance Handling
- Probability Estimation
- Model Serialization
- Machine Learning Inference
- Business Rule Evaluation
- Confidence Calibration
- Risk Assessment
- Human-in-the-Loop Decision Making
- REST API Model Serving
- Decision Audit Logging


---

# 🌟 Why Recruiters Like This Project

This project demonstrates the practical integration of machine learning with backend software engineering to solve a real-world fraud detection problem.

Instead of presenting only a trained model, the system showcases how machine learning can be deployed as part of a complete application by combining model inference, business decision logic, REST APIs, persistent storage, and an operational dashboard.

### Key Engineering Highlights

- End-to-End Machine Learning Solution
- Production-Style Backend Architecture
- RESTful API Development with FastAPI
- Modular Service-Oriented Design
- Machine Learning Inference Pipeline
- Business Rule Engine
- Decision Intelligence Layer
- Risk-Based Decision Making
- Confidence Calibration
- Human-in-the-Loop Workflow
- MySQL Data Persistence
- Decision Audit Logging
- Interactive Analytics Dashboard
- Object-Oriented Programming
- Reusable Components
- Clean Project Structure

---

# 🎯 Resume Keywords (ATS)

The following keywords accurately represent the technologies and concepts implemented in this project.

### Artificial Intelligence & Machine Learning

- Machine Learning
- Fraud Detection
- Binary Classification
- XGBoost
- Scikit-learn
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Evaluation
- Probability Estimation
- Machine Learning Inference
- Model Serialization
- Joblib

### Backend Engineering

- Python
- FastAPI
- REST API
- API Development
- Pydantic
- Uvicorn
- Backend Development

### Database

- MySQL
- Database Design
- SQL
- Data Persistence
- Audit Logging

### Software Engineering

- Object-Oriented Programming
- Modular Architecture
- Layered Architecture
- Service Layer
- Pipeline Pattern
- Clean Code
- Reusable Components

### Data Visualization

- Streamlit
- Plotly
- Dashboard Development
- Analytics Dashboard

---

# 💼 Interview Highlights

This project demonstrates practical experience in:

- Designing an end-to-end AI application
- Building machine learning inference services
- Developing RESTful APIs
- Integrating machine learning with backend systems
- Implementing business decision logic
- Designing relational database workflows
- Building operational dashboards
- Working with modular software architecture
- Applying object-oriented programming principles
- Handling class imbalance in machine learning
- Building reusable service components
- Deploying serialized machine learning models

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/ajaykichara/AI_Fraud_Decision_Intelligence_System.git
```

Move into the project directory.

```bash
cd AI_Fraud_Decision_Intelligence_System
```

Install project dependencies.

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

## Start the FastAPI Backend

```bash
python -m uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Launch the Streamlit Dashboard

```bash
python -m streamlit run dashboard/app_streamlit.py
```

---

# 📂 Application Workflow

```
Start Backend
        │
        ▼
Load Trained XGBoost Model
        │
        ▼
Launch Dashboard
        │
        ▼
Submit Transaction
        │
        ▼
Machine Learning Prediction
        │
        ▼
Decision Intelligence
        │
        ▼
Store Transaction
        │
        ▼
Log Decision
        │
        ▼
Human Review (If Required)
        │
        ▼
Dashboard Analytics
```

---

# 🚀 Future Roadmap

Potential enhancements for future versions include:

- Docker Containerization
- JWT Authentication & Authorization
- CI/CD Pipeline
- MLflow Integration
- Model Versioning
- Cloud Deployment
- Kubernetes Deployment
- Redis Caching
- Asynchronous Task Processing
- Kafka-Based Event Streaming
- Role-Based Access Control
- API Rate Limiting
- Configuration Management
- Automated Testing Pipeline
- Monitoring & Observability

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, open issues, or submit pull requests to help improve the project.

---

# 📄 License

This project is released for educational, learning, and portfolio purposes.

---

# 👨‍💻 Author

## Ajay Kichara

**Aspiring AI Engineer | Machine Learning Engineer | Backend Developer**

📧 Email

ajayajaykichara@gmail.com

🔗 GitHub

https://github.com/ajaykichara

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.