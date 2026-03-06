import streamlit as st
import pickle
import pandas as pd

# Load model and features
model = pickle.load(open("models/churn_model.pkl", "rb"))
features = pickle.load(open("models/model_features.pkl", "rb"))

st.title("Telco Customer Churn Prediction")

st.write("Enter customer details")
# Inputs
tenure = st.number_input("Tenure", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

# Predict button
if st.button("Predict"):

    # Create dataframe with same features as training
    sample = pd.DataFrame(columns=features)
    sample.loc[0] = 0

    sample["tenure"] = tenure
    sample["MonthlyCharges"] = monthly_charges
    sample["TotalCharges"] = total_charges

    prediction = model.predict(sample)

    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Stay")