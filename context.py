import json
import openai
import os
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv
from langchain.chat_models.azure_openai import AzureChatOpenAI
from langchain.schema import SystemMessage, HumanMessage


data = json.load(open('people.json', 'r'))

## LOAD .ENV FILE FOR API CONNECTION
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = "https://usedsatqs2aoa01.openai.azure.com/" 
openai.api_type = 'azure'
openai.api_version = "2023-03-15-preview"
deployment_name = 'gpt-35-turbo'

## INITIALIZE GPT 3.5
temp = 0
# GPT_35 = AzureChatOpenAI(deployment_name='gpt-35-turbo', model_name='gpt-35-turbo',temperature=temp)
GPT_4 = AzureChatOpenAI(deployment_name='gpt-4-32k', model_name='gpt-4-32k', temperature=temp)

# text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
# all_splits = text_splitter.split_documents(data)

# vectorstore = Chroma.from_documents(documents=all_splits,embedding=OpenAIEmbeddings())

# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# retriever=vectorstore.as_retriever()
# chat = ConversationalRetrievalChain.from_llm(GPT_35,retriever=retriever,memory=memory)

# result = chat({"question": "I'm looking to connect with someone with experience in scrum"})
# print(result)