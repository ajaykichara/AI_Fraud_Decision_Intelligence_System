import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Fraud Decision Intelligence System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "http://127.0.0.1:8000/decision/evaluate"

HISTORY_URL = "http://127.0.0.1:8000/decision/history"



def load_history():

    try:

        response = requests.get(HISTORY_URL)

        if response.status_code == 200:
            return response.json()

        return []

    except:
        return []


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🛡️ AFDIS")

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "💳 Evaluate Transaction",
            "📊 Decision History",
            "📈 Analytics"
        ]
    )

    st.markdown("---")

    st.subheader("API Status")

    try:

        response = requests.get(
            "http://127.0.0.1:8000/",
            timeout=5
        )

        if response.status_code == 200:

            st.success("🟢 FastAPI Connected")

        else:

            st.error("🔴 FastAPI Offline")

    except:

        st.error("🔴 FastAPI Offline")

    st.markdown("---")

    st.subheader("Model")

    st.info("XGBoost")

    st.markdown("---")

    st.subheader("Version")

    st.caption("Version 1.0")

# =====================================================
# HEADER
# =====================================================

st.title("🛡️ AI Fraud Decision Intelligence System (AFDIS)")

st.caption(
    "Real-Time AI-Powered Fraud Decision Support Dashboard"
)

st.divider()

# =====================================================
# DASHBOARD
# =====================================================

if page == "🏠 Dashboard":

    history = load_history()

    total_transactions = len(history)

    approved = sum(
        1 for item in history
        if item["final_decision"] == "APPROVE"
    )

    rejected = sum(
        1 for item in history
        if item["final_decision"] == "REJECT"
    )

    manual_review = sum(
        1 for item in history
        if item["final_decision"] == "MANUAL_REVIEW"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Transactions",
        total_transactions
    )

    c2.metric(
        "Approved",
        approved
    )

    c3.metric(
        "Rejected",
        rejected
    )

    c4.metric(
        "Manual Review",
        manual_review
    )

    st.divider()

    left, right = st.columns([2,1])

    with left:

        st.subheader("System Overview")

        try:

            response = requests.get(
                "http://127.0.0.1:8000/",
                timeout=5
            )

            if response.status_code == 200:

                api_status = "🟢 Online"

            else:

                api_status = "🔴 Offline"

        except:

            api_status = "🔴 Offline"

        st.write(f"**Backend :** FastAPI ({api_status})")

        st.write("**Machine Learning Model :** XGBoost")

        st.write("**Database :** MySQL")

        st.write("**Prediction Engine :** Active")

        st.write("**Decision Engine :** Active")

    with right:

        if total_transactions == 0:

            gauge_value = 0

        else:

            gauge_value = round(
                approved / total_transactions * 100
            )

        fig = go.Figure(
            go.Indicator(

                mode="gauge+number",

                value=gauge_value,

                title={
                    "text":"Approval Rate (%)"
                },

                gauge={

                    "axis":{
                        "range":[0,100]
                    }

                }

            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    if total_transactions > 0:

      st.subheader("Recent Decisions")

      df = pd.DataFrame(history)

      styled_df = (
        df.head(8)
        .style
        .set_properties(
             **{
               "color": "white",
               "background-color": "black" }))

      st.dataframe(
            styled_df,
            use_container_width=True,
            hide_index=True)

    else:
        st.info("No transactions processed yet.")
# =====================================================
# EVALUATE PAGE
# =====================================================

elif page == "💳 Evaluate Transaction":

    st.header("Transaction Information")

    left, right = st.columns(2)

    with left:

        merchant = st.text_input("Merchant")

        merchant_category = st.text_input("Merchant Category")

        transaction_amount = st.number_input(
            "Transaction Amount",
            min_value=0.0
        )

        gender = st.selectbox(
            "Gender",
            ["M","F"]
        )

        city = st.text_input("City")

        state = st.text_input("State")

        customer_zip = st.number_input(
            "Customer ZIP",
            step=1
        )

        city_population = st.number_input(
            "City Population",
            step=1
        )

    with right:

        job = st.text_input("Job")

        merchant_zip = st.number_input(
            "Merchant ZIP",
            step=1
        )

        customer_age = st.slider(
            "Customer Age",
            18,
            100,
            30
        )

        transaction_hour = st.slider(
            "Transaction Hour",
            0,
            23,
            12
        )

        transaction_day = st.slider(
            "Transaction Day",
            1,
            31,
            15
        )

        transaction_month = st.slider(
            "Transaction Month",
            1,
            12,
            6
        )

        transaction_weekday = st.slider(
            "Transaction Weekday",
            0,
            6,
            2
        )

        is_weekend = st.checkbox("Weekend")

        is_night_transaction = st.checkbox(
            "Night Transaction"
        )

        high_amount_transaction = st.checkbox(
            "High Amount Transaction"
        )

    st.divider()

    submit = st.button(
    "🚀 Evaluate Transaction",
    use_container_width=True
    )

    if submit:

        transaction = {

            "merchant": merchant,
            "merchant_category": merchant_category,
            "transaction_amount": transaction_amount,
            "gender": gender,
            "city": city,
            "state": state,
            "customer_zip": int(customer_zip),
            "city_population": int(city_population),
            "job": job,
            "merchant_zip": int(merchant_zip),
            "customer_age": customer_age,
            "transaction_hour": transaction_hour,
            "transaction_day": transaction_day,
            "transaction_month": transaction_month,
            "transaction_weekday": transaction_weekday,
            "is_weekend": is_weekend,
            "is_night_transaction": is_night_transaction,
            "high_amount_transaction": high_amount_transaction

        }

        with st.spinner("Evaluating Transaction..."):

            try:

                response = requests.post(
                    API_URL,
                    json=transaction,
                    timeout=30
                )

                if response.status_code == 200:

                    result = response.json()


                    st.success("Transaction Evaluated Successfully")
                    st.divider()

                    st.header("🎯 Prediction Summary")

                    decision = result["final_decision"]

                    # ======================================================
                    # Decision Banner
                    # ======================================================

                    if decision == "APPROVE":

                        st.success("✅ FINAL DECISION : APPROVE")

                    elif decision == "REJECT":

                        st.error("⛔ FINAL DECISION : REJECT")

                    else:

                        st.warning("⚠️ FINAL DECISION : MANUAL REVIEW")

                    # ======================================================
                    # Metrics
                    # ======================================================

                    col1, col2, col3, col4 = st.columns(4)

                    col1.metric(
                        "Prediction",
                        result["model_prediction"]
                    )

                    col2.metric(
                        "Confidence",
                        f"{result['confidence_score']:.2%}"
                    )

                    col3.metric(
                        "Risk Level",
                        result["risk_level"]
                    )

                    col4.metric(
                        "Risk Score",
                        result["risk_score"]
                    )

                    st.divider()

                    col5, col6 = st.columns(2)

                    col5.metric(
                        "Confidence Zone",
                        result["confidence_zone"]
                    )

                    col6.metric(
                        "Decision",
                        result["final_decision"]
                    )

                    # ======================================================
                    # Progress Bar
                    # ======================================================

                    st.subheader("Confidence Score")

                    st.progress(result["confidence_score"])

                    st.write(
                        f"{result['confidence_score']:.2%}"
                    )

                    # ======================================================
                    # Override Reason
                    # ======================================================

                    st.subheader("Decision Explanation")

                    st.info(result["override_reason"])

                    # ======================================================
                    # Transaction Details
                    # ======================================================

                    with st.expander("Transaction Details"):

                        st.json(transaction)

                    # ======================================================
                    # API Response
                    # ======================================================

                    with st.expander("Prediction Response"):

                        st.json(result)
                else:

                    st.error(response.text)

            except Exception as e:

                st.error(e)

# =====================================================
# HISTORY
# =====================================================

elif page == "📊 Decision History":

    st.header("📊 Decision History")

    history = load_history()

    if len(history) == 0:

         st.warning("No transactions processed yet.")

    else:

        df = pd.DataFrame(history)

        st.subheader("Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total Records",
            len(df)
        )

        c2.metric(
            "Average Confidence",
            f"{df['model_confidence'].mean():.2%}"
        )

        c3.metric(
            "Average Risk Score",
            round(df["risk_score"].mean(),2)
        )

        st.divider()

        st.subheader("Decision Log")

        styled_df = df.style.set_properties(
        **{
        "color": "white",
        "background-color": "black"
        })

        st.dataframe(
           styled_df,
           use_container_width=True,
           hide_index=True
        )

        st.download_button(

            label="📥 Download CSV",

            data=df.to_csv(index=False),

            file_name="decision_history.csv",

            mime="text/csv"

        )

# =====================================================
# ANALYTICS
# =====================================================

elif page == "📈 Analytics":

    st.header("📈 Analytics Dashboard")

    history = load_history()

    if len(history) == 0:

         st.warning("No transaction data available.")

    else:

        df = pd.DataFrame(history)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("Decision Distribution")

            decision_count = (
                df["final_decision"]
                .value_counts()
                .reset_index()
            )

            decision_count.columns = [
                "Decision",
                "Count"
            ]

            fig = px.pie(

                decision_count,

                names="Decision",

                values="Count",

                hole=0.5,

                title="Final Decisions"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col2:

            st.subheader("Risk Level")

            risk_count = (
                df["risk_level"]
                .value_counts()
                .reset_index()
            )

            risk_count.columns = [
                "Risk",
                "Count"
            ]

            fig = px.bar(

                risk_count,

                x="Risk",

                y="Count",

                color="Risk",

                title="Risk Distribution"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.divider()

        col3, col4 = st.columns(2)

        with col3:

            st.subheader("Confidence Scores")

            fig = px.histogram(

                df,

                x="model_confidence",

                nbins=20,

                title="Confidence Distribution"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col4:

            st.subheader("Risk Score")

            fig = px.histogram(

                df,

                x="risk_score",

                nbins=10,

                title="Risk Score Distribution"

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )