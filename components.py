## IMPORT STREAMLIT
import streamlit as st


## PAGE HEADER
def setup_page():
    st.set_page_config(
        page_title = "Welcome",
        layout = "wide",
        page_icon = "🏡",
        initial_sidebar_state="expanded",
    )


## LOGO 
def display_logo():
    st.image("logo.png", width = 700)


## INPUT FIELD 
def user_input_field():
    user_prompt = st.text_input("Try me!", key="user_prompt")
    return user_prompt
