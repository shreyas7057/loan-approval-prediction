import streamlit as st
import pandas as pd
import pickle

data = pd.read_csv("loan_approval_dataset.csv")
model = pickle.load(open('loanapproval_model.pkl','rb'))


st.title("Loan Approval Prediction")

st.write("Enter the following information to predict whether loan will be approved or not:")

dependents = st.number_input("Number of Dependents", min_value=1, max_value=100, value=30)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
annual_income = st.number_input("Annual Income", min_value=0,value=0)
loan_ammount = st.number_input("Loan Amount",min_value=0,value=0)
loan_term = st.number_input("Loan Term",min_value=0,value=0)
cibil_score = st.number_input("Cibil Score",min_value=0,value=0)
movable_assets = st.number_input("Movable Assets",min_value=0,value=0)
immovable_assets =st.number_input("Immovable Assets",min_value=0,value=0)

education_encoded = 0 if education == "Not Graduate" else 1
self_employed_encoded = 1 if self_employed == "Yes" else 0


data = pd.DataFrame([[dependents, education_encoded, self_employed_encoded, annual_income, loan_ammount, loan_term,cibil_score,movable_assets,immovable_assets]],
                        columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term','cibil_score','Movable_Assets','Immovable_Assets'])


if st.button("Predict"):
    prediction = model.predict(data)
    if prediction==0:
        st.write("Loan Not Approved")
    else:
        st.write("Loan Approved")