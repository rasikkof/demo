import streamlit as st
import datetime
st.title('r.j college')
st.header('master application')
name = st.text_input('enter your name')
f = st.text_input('enter your father name')
m = st.text_input('enter your mother name')

st.text('       ')
g = st.selectbox('Gender',('male','female','trans','other'))

st.text('    ')
st.text('Qaulification')
option_1= st.checkbox('10th')
option_2= st.checkbox('12th')
option_3= st.checkbox('degree')
option_4= st.checkbox('msc')
option_5= st.checkbox('phd')

st.text('       ')
st.text_area('write your SOP', max_chars=150)

st.text('    ')
d=st.date_input('DOB', datetime.date(2023,1,1))
st.write('your DOB: ',d)

st.text('    ')
if(st.button('submit')):
    st.warning('your form has been submitted')
    st.write('name : ', name)
    st.write('father name : ', f)
    st.write('Mother name : ', m)
    st.write('Gendre : ', g)
    st.write('DOB: ', d)