# Telco Customer Churn Prediction

## Project Overview
This project predicts whether a telecom customer will **churn (leave the service)** or **stay** using Machine Learning.  
A **Streamlit web application** is built to allow users to input customer details and get churn predictions instantly.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Dataset
The dataset used in this project is the **Telco Customer Churn Dataset**, which contains customer information such as:

- Gender
- Senior Citizen
- Tenure
- Monthly Charges
- Contract Type
- Internet Service
- Payment Method

---

## Machine Learning Model
The model was trained using **Scikit-learn** and saved using **Pickle**.

Model files:
- churn_model.pkl
- scaler.pkl
- model_features.pkl

---

## Streamlit Web App
The machine learning model is deployed using Streamlit to create an interactive web application.

Users can:
- Enter customer information
- Click the predict button
- Get a prediction whether the customer will churn or stay

## How to Run the App

Install required libraries

pip install -r requirements.txt

Run the Streamlit app

streamlit run app.py

Then open in browser

[http://localhost:8501](http://localhost:8501)

## Author
Himanshu Bisht
