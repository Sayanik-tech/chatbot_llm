from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
import streamlit as st

## define a prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question "),
        ("user","Question:{question}")
    ])

## setrup the stramlit framework
st.title("Sayanik's GPT")
input_text = st.text_input("Ask your Question")

## initialize the ollama model
llm = OllamaLLM(model="llama2")

chain = prompt|llm

## invoke the chain with the input text and display the output
if input_text:
    st.write(chain.invoke({"question":input_text}))