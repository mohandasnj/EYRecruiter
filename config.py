## IMPORT NECESSARY PACKAGES 
import os
import openai
import streamlit as st
from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models.azure_openai import AzureChatOpenAI

## LOAD .ENV FILE FOR API CONNECTION
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = "https://usedsatqs2aoa01.openai.azure.com/" 
openai.api_type = 'azure'
openai.api_version = "2023-03-15-preview"
deployment_name = 'gpt-35-turbo'

## INITIALIZE GPT 3.5
temp = 0
GPT_35 = AzureChatOpenAI(deployment_name='gpt-35-turbo', model_name='gpt-35-turbo',temperature=temp)
