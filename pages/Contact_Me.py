import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='contact_me_form', clear_on_submit=True):
    user_email = st.text_input(label='Your email adress:', key='emailInput')
    user_message = st.text_area('Your message:', key='messageInput')
    submitted = st.form_submit_button('Submit')
    if submitted:
        send_email(user_message, user_email)
        st.info('Email has been sent.')
