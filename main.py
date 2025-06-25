import streamlit as st
import pandas as pd
from src.fraud_detector import detect_fraud_callers
from src.visualizer import generate_visuals

st.title("Telecom Fraud Detection System")

uploaded_file = st.file_uploader("Upload Call Data CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    fraud_callers, caller_flags = detect_fraud_callers(df)

    st.success(f"Fraud Detection Complete. {len(fraud_callers)} suspicious callers found.")

    st.write("Suspected Fraud Callers")
    results_df = pd.DataFrame({
        'caller_id': list(fraud_callers),
        'rules_triggered': [caller_flags[c] for c in fraud_callers]
    })
    st.dataframe(results_df)

    results_df.to_csv("reports/suspected_fraud.csv", index=False)

    st.write("Visualizations")
    generate_visuals(df)