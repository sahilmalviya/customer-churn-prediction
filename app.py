import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("churn_model.pkl")
columns = joblib.load("columns.pkl")

st.title("📊 Customer Churn Prediction")

# User inputs (simple)
tenure = st.slider("Tenure", 0, 72)
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

if st.button("Predict"):

    # Create input dataframe
    input_data = pd.DataFrame([[0]*len(columns)], columns=columns)

    input_data["tenure"] = tenure
    input_data["MonthlyCharges"] = monthly
    input_data["TotalCharges"] = total

    result = model.predict(input_data)

    if result[0] == 1:
        st.error("🚨 Customer will CHURN")
    else:
        st.success("✅ Customer will STAY")