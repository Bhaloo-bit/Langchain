import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st 

llm = ChatGroq(
    model ="openai/gpt-oss-20b",
    api_key= os.getenv("GROQ_API_KEY")
)


st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))


st.header("Groq Ai chatbot")
query =  st.chat_input("Ask Anything:")
if query:
    st.session_state.messages.append(["user", query])
    st.chat_message("user").markdown(query)
    response = llm.invoke(st.session_state.messages)
    print("AI", response.content)
    st.session_state.messages.append(["AI", response.content])
    st.chat_message("AI").markdown(response.content)

print(st.session_state.messages)