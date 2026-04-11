import streamlit as st                
import requests 

st.title('Live currency coverter')
indrs=st.number_input("Enter indian rs: ",min_value=1)

seleccur=st.selectbox('enter selected currency ',['USD','EUR','JPY','GBP'])


if st.button('Convert'):
    url='https://api.exchangerate-api.com/v4/latest/INR'
    
    responce=requests.get(url)
    
    if responce.status_code==200:
        data=responce.json()
        rate=data['rates'][seleccur]
        st.success(f'COnverted currency of {seleccur} in ind rs is: {rate*indrs}')
    else:
        st.error('failed to convert')
