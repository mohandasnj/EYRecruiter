import streamlit as st

## IMPORT ALL NECESSARY COMPONENTS FROM CONFIG.PY AND UI.PY
from config import *
from context import *

## RENDER UI COMPONENTS
st.set_page_config(
        page_title = "Welcome",
        layout = "wide",
        page_icon = "🏡",
        initial_sidebar_state="expanded",
    )

st.title("EYRecruiter")

## RENDER USER INPUT AND DEFINE HANDLER 
user_prompt = st.text_input("Find a connection!", key="user_prompt")

## SYSTEM PROMPT 
# system_prompt = "Assistant helps user with finding an employee based on input criteria"

## HANDLE USER INPUT 
if user_prompt:
    # print(user_prompt)
    response = GPT_4([
        SystemMessage(content=f"Here is the people data structured as JSON:\n{data}"), 
        HumanMessage(content=user_prompt + "  Please put any JSON lists in sentence form. Please format your response to use Markdown to add emphasis to sections.")]).content

    ## DISPLAY RESPONSE 
    st.markdown(response)  
