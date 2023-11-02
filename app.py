import streamlit as st
import pygsheets

gc = pygsheets.authorize(service_file='path/to/your/service_account.json')

# Open the Google Spreadsheet using its title
spreadsheet = gc.open('TBL-Data')

# Select a worksheet
worksheet = spreadsheet.sheet1

# Get all values in the worksheet
values = worksheet.get_all_values()

# Create a dictionary of usernames and passwords
credentials = {row[0]: row[1] for row in values}

username = st.text_input('Username')
password = st.text_input('Password', type='password')

if st.button('Login'):
    if username in credentials and credentials[username] == password:
        st.success('Logged in successfully')
    else:
        st.error('Invalid credentials')
