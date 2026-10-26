import streamlit as st
import pickle
import pandas as pd
with open('pipeline.pkl','rb') as f:
  model=pickle.load(f)

st.title('LOAN APPROVAL SYSTEM')
dependents=st.number_input('Number of Dependents',0,7,2)
education= st.selectbox('Select Your Education',[' Graduate',' Not Graduate'])
self_employed= st.selectbox('Are you self employed?',[' Yes',' No'])
income_annum=st.number_input('Income per annum',0,value=100000)
loan_amount=st.number_input('Loan Amount Required',0,value=100000)
loan_term=st.number_input('Loan Timeperiod (months): ',1,value=4)
cibil_score=st.number_input('Cibil Score: ',300.0,900.0)
assets_value=st.number_input('Enter your overall Assets Value: ',0,value=840000)
def predict(d,e,se,i_a,l_a,l_t,c_s,a_v):
  user_input = {
    ' no_of_dependents': [d],
    ' education': [e],
    ' self_employed': [se],
    ' income_annum': [i_a],
    ' loan_amount': [l_a],
    ' loan_term': [l_t],
    ' cibil_score': [c_s],
    'assets_value': [a_v]
  }
  datapoint=pd.DataFrame(user_input)
  prediction=model.predict(datapoint)[0]
  if prediction==0:
    return "Approved"
  return "Rejected"

if st.button('Is Loan Approved?'):
  approval=predict(dependents,education,self_employed,income_annum,loan_amount,loan_term,cibil_score,assets_value)
  st.write(f"Your Loan is {approval}")
