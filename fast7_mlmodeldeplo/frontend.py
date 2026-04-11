import streamlit as st                        
import requests

API_URL="http://127.0.0.1:8000/predict"

age=st.number_input("Age(Yers)",min_value=1,max_value=120)
weight=st.number_input("Weight(KG)",min_value=1,max_value=300)
height=st.number_input("Height(M)")
income_lpa=st.number_input("Income(LPA)",min_value=0)
smoker=st.selectbox("Are You Smoker",[True,False])
city=st.text_input("City")
occupation = st.selectbox("Occupation",['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])


if st.button('Predict Category'):
    input_data={
            'age':age,
            'weight':weight,
            'height':height,
            'income_lpa':income_lpa,
            'smoker':smoker,
            'city':city,
            'occupation':occupation
         }
  
    
    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"🎯 Predicted Category: {result['PREDICTION IS: ']}")
        else:
            st.error(f"API Error ❌ Status: {response.status_code}\nDetails: {response.text}")

    except Exception as e:
        st.error(f"API Request Failed ⚠\nError: {str(e)}")

  