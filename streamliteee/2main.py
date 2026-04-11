import streamlit as st                          

st.title('Simple form')

if st.button('Click me to Start'):
    st.success('Lets go')
    
st.checkbox('Click me if you are 18+')

rd=st.radio('select your domain',[None,'python','java','c++','ml/ds'])
if rd:
    st.success(f'lets start {rd}')

sb=st.selectbox('what do like most',['DSA','DEV'])
st.write(f'Good you like {sb}')

sl=st.slider('enter your previous knowledge out of 10',0,10,0)
if sl:
    st.success(f'lets startf from {sl}')
    
    
name=st.text_input('enter you full name')    
no=st.number_input('enter you pointer!',max_value=100,min_value=0)
dob=st.date_input('enter your date of birth')


st.write(f'name:{name}')
st.write(f'dob:{dob} ')
st.write(f'pointer:{no}')
