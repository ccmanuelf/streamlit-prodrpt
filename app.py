import streamlit as st
from streamlit_authenticator import Authenticator

authenticator = Authenticator()

username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if authenticator.check_credentials(username, password):
        st.success('Logged in successfully')
    else:
        st.error('Invalid credentials')
