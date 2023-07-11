## IMPORT ALL NECESSARY COMPONENTS FROM CONFIG.PY AND UI.PY
from config import *
from components import *

## RENDER UI COMPONENTS
setup_page()
display_logo()

## RENDER USER INPUT AND DEFINE HANDLER 
user_prompt = user_input_field()

## SYSTEM PROMPT 
system_prompt = "Assistant welcomes participants to the GenAI Hackathon"

## HANDLE USER INPUT 
if user_prompt:
    response = GPT_35([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]).content

    ## DISPLAY RESPONSE 
    st.text(response)  
