import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import streamlit_authenticator as stauth

st.title("Novalink Production Report")

# Placeholder pages/functions.
def home_page():
    st.subheader('Home')
    st.info('This is your Home page.')

def page_2():
    st.subheader('Page 2')
    st.success('Welcome to Page 2!')

# Establishing a Google Sheets connection using "connection.gsheets" from secrets.toml.
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Fetching data from google sheet into pandas dataframe 
credentials_df = conn.read(worksheet="Sheet1")
st.dataframe(credentials_df)

"""
usernames = credentials_df['username'].tolist()

# Hash passwords (assuming they are stored in plain text which is not recommended for production)
hashed_passwords_dict = {name: stauth.Hasher().hash(password) for name, password in zip(usernames, credentials_df['password'])}

# Set up authenticator instance with hashed passwords dictionary.
cookie_expiry_days=30 

authenticator_component=stauth.Authenticate(
    names=usernames,
    hashes=list(hashed_passwords_dict.values()),
    cookie_name="streamlit_auth",
	key='some_random_string', # A random string acts like a signing key to make cookies secure. Replace it with an actual random string.
	cookie_expiry_days=cookie_expiry_days,
	preauthorized_emails=None)  

name, authentication_status,_ \
    	= authenticator_component.login('Login', 'main')

if authentication_status:
	st.sidebar.title(f"Welcome {name}")
	page_names_to_funcs={
	    "Home": home_page,
	    "Page 2": page_2,
	}
	
	selected_page_label_selected_by_user_via_dropdown_menu_widget_on_sidebar\
	    	  =(list(page_names_to_funcs.keys())[0] if (len(list(page_names_to_funcs.keys()))>0)\
	    	  		else "") if ("selected_option_label_selected_by_user_via_dropdown_menu_widget_on_sidebar"\
	    	  			not in list(st.session_state.keys())) else \
		    	          	  				st.session_state.selected_option_label_selected_by_user_via_dropdown_menu_widget_on_sidbar
		
	with 	st.sidebar.container():
		 selected_page_label_selected_by_user_via_dropdown_menu_widget_on_sidebar\
		 	  =(list(page_names_to_funcs.keys())[0] if (len(list(page_names_to_funcs.keys()))>0)\
		 	  		else "") if ("selected_option_label_selected_by_user_via_dropdown_menu_widget_on_sidebar"\
		 	  			not in list(st.session_state.keys())) else \
		    	          	  				selected_pge_optn_lbl_slctd_usr_drpdwn_widgt_sbdr
		
	page_func_t_cl_bsd_upon_th_abv_selction_md_usng_th_drp_dwn_slector_in_cntr_abov()	

elif authentication_status == False:
	st.error('Username/password is incorrect')

elif authentication_status == None:
	st.warning('Please enter your username and password')
"""
