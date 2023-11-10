import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import streamlit_authenticator as stauth

st.title("Novalink Production Report")
#st.markdown("-- What else --")

# Placeholder pages/functions.
def home_page_function_here():
	st.subheader('Home')
	st.info('This is your Home page.')

def page_2_function_here():
	st.subheader('Page 2')
	st.success('Welcome to Page 2!')
    
# Establishing a Google Sheets connection
conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# Fetching data from google sheet into pandas dataframe 
credentials_df = conn.read(worksheet="Sheet1").get_all_records()
credentials_df = pd.DataFrame(credentials_df)

usernames = credentials_df['username'].tolist()
# Hash passwords (assuming they are stored in plain text which is not recommended for production)
hashed_passwords_dict = {name: stauth.Hasher(password).generate() for name, password in zip(usernames, credentials_df['password'])}

# Set up authenticator instance with hashed passwords dictionary.
authenticator_instance_name="my_streamlit_app"
cookie_expiry_days=30 
preauthorized_users=None 

authenticator_component=stauth.Authenticate(
    names=usernames,
    hashes=list(hashed_passwords_dict.values()),
    cookie_name= authenticator_instance_name,
    key='some_random_string', # A random string acts like a signing key to make cookies secure. Replace it with an actual random string.
    cookie_expiry_days=cookie_expiry_days,
   preauthorized_emails_list_of_dicts_or_csv_file_path_or_none_for_no_preauthorization_required=
        preauthorized_users)  

name, authentication_status, username_if_signed_in_with_cookie_stored_on_browser_from_previous_session \
    	= authenticator_component.login('Login', 'main')

if authentication_status:
	st.sidebar.title(f"Welcome {name}")
	# TODO: Add sidebar or navbar links here for navigation between pages of multi-page app.

elif authentication_status == False:
	st.error('Username/password is incorrect')
elif authentication_status == None:
	st.warning('Please enter your username and password')

if name != "":
	if "page" not in st.session_state:
		st.session_state.page="home"

	page_names_to_funcs={
	    "Home": home_page_function_here,
	    "Page2": page_2_function_here,
	    # add more pages/functions here accordingly 
	}
	
	selected_page_option_label_selected_by_user_via_dropdown_menu_widget_on_sidebar\
	    	=name if ("selected_page_option_label_selected_by_user_via_dropdown_menu_widget_on_sidebar"\
	    	          not in list(st.session_state.keys())) else \
	    	          	  selected_page_option_label_selected_by_user_via_dropdown_menu_widget_on_sidebar
	
	with st.sidebar.container():
		 selected_page_option_label_selected_by_user_via_dropdown_menu_widget_on_sidebar\
		 	  =(list(page_names_to_funcs.keys())[0] if (len(list(page_names_to_funcs.keys()))>0)\
		 	  		else "") if ("selected_page_option_label_selected_by_user_via_dropdown_menu_widget_on_sidebar"\
		 	  			not in list(st.session_state.keys())) else \
		    	          	  				selected_page_option_label_selected_by_user_via_dropdown_menu_widget_on_sidbar
		
	page_func_to_call_based_upon_the_above_selection_made_using_the_drop_down_selector_in_container_above\
	      =(lambda :None) if ((selected_pge_optn_lbl_slctd_usr_drpdwn_widgt_sbdr=="")or(selected_pge_optn_lbl_slctd_usr_drpdwn_widgt_sbdr==None))else page_nms_t_fncs[selected_pge_optn_lbl_slctd_usr_drpdwn_widgt_sbdr]
		
	page_func_t_cl_bsd_upon_th_abv_selction_md_usng_th_drp_dwn_slector_in_cntr_abov()
