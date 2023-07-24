import streamlit as st

## IMPORT ALL NECESSARY COMPONENTS FROM CONFIG.PY AND UI.PY
from config import *

import json
import openai
import os
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv


data = json.load(open('people.json', 'r'))

## LOAD .ENV FILE FOR API CONNECTION
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = "https://usedsatqs2aoa07.openai.azure.com/" 
openai.api_type = 'azure'
openai.api_version = "2023-03-15-preview"
deployment_name = 'gpt-35-turbo'

## RENDER UI COMPONENTS
st.set_page_config(
        page_title = "Welcome",
        layout = "wide",
        page_icon = "🏡",
        initial_sidebar_state="expanded",
    )

st.title("EYRecruiter")

user_prompt = st.text_input("Find a connection!", key="user_prompt")



@st.cache_data
def chat(user_prompt):
    ## RENDER USER INPUT AND DEFINE HANDLER 


    ## SYSTEM PROMPT 
    # system_prompt = "Assistant helps user with finding an employee based on input criteria"

    ## HANDLE USER INPUT         # print(user_prompt)
    response = openai.ChatCompletion.create(
        engine="gpt-4-32k",
        messages=[
            {"role": "system", "content": "You are assisting a user to find an employee from a JSON dataset based on given criteria. You may only use the provided dataset, and be sure to consider the entire dataset when generating responses. Never respond with a person if their criteria don't match the prompt."},
            {"role": "assistant", "content": f"When displaying names, make sure to include contact information as well. Use Markdown to add emphasis to relevant sections of your response. Do not output lists in JSON format, instead display them only as english sentences. The dataset is structured as JSON, and is attached below: \n {data}"},
            {"role": "user", "content": user_prompt}
        ]
    )
    ## DISPLAY RESPONSE 
    st.markdown(response['choices'][0]['message']['content'])  

if user_prompt:
    chat(user_prompt)