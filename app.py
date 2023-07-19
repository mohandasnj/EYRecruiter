import streamlit as st

## IMPORT ALL NECESSARY COMPONENTS FROM CONFIG.PY AND UI.PY
from config import *
from context import chat

## RENDER UI COMPONENTS
st.set_page_config(
        page_title = "Welcome",
        layout = "wide",
        page_icon = "🏡",
        initial_sidebar_state="expanded",
    )

st.image("logo.png", width = 700)

st.title("hi")

## RENDER USER INPUT AND DEFINE HANDLER 
user_prompt = st.text_input("Find a connection!", key="user_prompt")

## SYSTEM PROMPT 
# system_prompt = "Assistant helps user with finding an employee based on input criteria"

## HANDLE USER INPUT 
if user_prompt:
    # print(user_prompt)
    response = chat({"question": user_prompt})


    ## DISPLAY RESPONSE 
    st.text(response["answer"])  
