import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


model = joblib.load("model.pkl")  #  use trained RandomForest model

# Load dataset for mean values
df = pd.read_csv("diabetes.csv")      ## load dataset 

## determine sympotms and risk factor of diabetes in sidebar
st.sidebar.header("About Diabetes")
st.sidebar.write("""Diabetes is a chronic condition affecting blood sugar levels.
**Symptoms:**  Frequent urination, increased thirst, fatigue.  
**Risk Factors:**  Obesity, age, family history, lifestyle.
""")

## name title
st.title("Simple Diabetes Prediction App")


st.header("Enter Patient Details")

preg = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose", 0, 200, 120)
bp = st.number_input("Blood Pressure", 0, 140, 70)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
age = st.number_input("Age", 0, 120, 30)


# Ensure same order of columns as training dataset
new_patient = pd.DataFrame([{
    'Pregnancies': preg,
    'Glucose': glucose,
    'BloodPressure': bp,
    'SkinThickness': df['SkinThickness'].mean(),
    'Insulin': df['Insulin'].mean(),
    'BMI': bmi,
    'DiabetesPedigreeFunction': df['DiabetesPedigreeFunction'].mean(),
    'Age': age
}])

# Reorder columns to match training
new_patient = new_patient[df.drop("Outcome", axis=1).columns]



if st.button("Predict"):
    pred = model.predict(new_patient)[0]
    prob = model.predict_proba(new_patient)[0]
    result = "Diabetes" if pred==1 else "No Diabetes"
    
    st.subheader(f"Prediction: {result}")

   
    plt.figure(figsize=(5,3))
    sns.barplot(x=["No Diabetes","Diabetes"], y=prob)
    plt.ylim(0,1)                                              ## limit of y-axis
    plt.title("Prediction Probability")
    st.pyplot(plt)
