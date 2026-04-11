#working with pandas  
import streamlit as st                  
import pandas as pd                      

file=st.file_uploader('upload csv file ',type=['csv'])

if(file):
    df=pd.read_csv(file)
    
if file:
    ff=df.head(5)
    st.header('first five')
    st.write(df.tail(5))
    st.header('last five')
    st.write(df.head(5))
    st.write(ff[['Name','Age','Ticket']])
    st.header('describe')
    st.write(df.describe())

    st.header('dataframe')
    st.dataframe(df.head(10))

if file:
    gender=st.selectbox('select the gender whic you want to see data',df['Sex'].unique())
    st.dataframe(df[df['Sex']==gender])

