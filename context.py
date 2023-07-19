from langchain.document_loaders import JSONLoader
from langchain.memory import ConversationBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv
from langchain.schema import SystemMessage, HumanMessage
from langchain.chat_models.azure_openai import AzureChatOpenAI

import json
import openai
import os
from pathlib import Path
from pprint import pprint

loader = JSONLoader(
    file_path='./people.json',
    jq_schema='.[].person_string')

data = loader.load()

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

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(data)

vectorstore = Chroma.from_documents(documents=all_splits,embedding=OpenAIEmbeddings())

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

retriever=vectorstore.as_retriever()
chat = ConversationalRetrievalChain.from_llm(GPT_35,retriever=retriever,memory=memory)

result = chat({"question": "I'm looking to connect with someone with experience in scrum"})
print(result)