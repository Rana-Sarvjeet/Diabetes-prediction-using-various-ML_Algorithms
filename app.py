import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

df = pd.read_csv("df_filtered.csv") 
st.title("Diabetes Prediction")
col1 , col2 ,col3=st.columns(3)

with col1:
    Glucose = st.number_input(
        "enter the GLUCOSE level (mg/dL):",
        min_value=1,
        max_value=300,
        step=1
    )
with col2:
    BloodPressure = st.number_input(
        "enter BloodPressure:",
        min_value=10,
        max_value=140,
        step=1
    )
with col3:
    SkinThickness = st.number_input(
        "enter the SkinThickness:",
        min_value=1,
        max_value=120,
        step=1
    )
col1 , col2 ,col3=st.columns(3)
with col1:
    Insulin = st.number_input(
        "enter the Insulin:",
        min_value=1,
        max_value=500,
        step=1
    )
with col2:
    BMI = st.number_input(
        "enter BMI:",
        min_value=10,
        max_value=140,
        step=1
    )
with col3:
    DiabetesPedigreeFunction = st.number_input(
        "Enter DiabetesPedigreeFunction:",
        min_value=0.0,
        max_value=3.0,
        value=0.0,          
        step=0.001,          
        format="%.3f"
    )
col1 =st.columns(1)[0]
with col1:
    Age = st.number_input(
        "enter the age:",
        min_value=10,
        max_value=100,
        step=1
    )

feature_names = df.columns.tolist()

if st.button("Predict"):

    input_data = np.array([[Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]], dtype=np.float64)
    # Make prediction
    
    input_data_scaled = scaler.transform(input_data)

# Predict
    prediction = model.predict(input_data_scaled)

    # Display result
    if prediction[0] == 1:
        st.error("⚠️ The person is **likely diabetic**.")
    else:
        st.success("✅ The person is **not diabetic**.")







    

    

    

    
