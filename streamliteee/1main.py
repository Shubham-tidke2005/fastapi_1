import streamlit as st                 

st.title('hello How are you')
st.subheader('hiiiiiiiiiii what are you doing')
st.text('dd dsvd dfsdg dsf')
st.write('ok byy')


sub=st.selectbox('you fav subject!',[None,'maths','english','history','science','arts'])

if sub:
    st.text('Thank you for your feedback')