import streamlit as st    


st.title('CHOOSE THE WRITE PATH')                      

col1,col2=st.columns(2)

with col1:
    st.header('DATA STRUCTURE')
    st.image('https://c8.alamy.com/comp/GNB4H9/word-cloud-data-structure-GNB4H9.jpg',width=200)
    v1=st.button('START DSA')
    
with col2:
    st.header('DEVLOPMENT')
    st.image('https://thumbs.dreamstime.com/b/web-development-coding-programming-internet-technology-business-concept-web-development-coding-programming-internet-technology-121903546.jpg',width=200)
    v2=st.button('START DEV')

if v1:
    st.success('voted for DSA')
else: 
    st.success('voted for DEV')
    
name=st.sidebar.text_input('Enter name: ')
age=st.sidebar.number_input('Enter age: ')

with st.expander('Road map'):
    st.write('''
             1.Comple the basic datastructure such as array and string \n
             2.complete your dev in java and springboot   \n
             3.later other advance data structure
             ''')

if name:
    st.text(f'Thank You {name} for your opinion')
st.markdown('OK byyyyyyyyyyyyyyyyyy')

