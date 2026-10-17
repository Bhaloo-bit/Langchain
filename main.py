import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model ="openai/gpt-oss-20b",
    api_key= os.getenv("GROQ_API_KEY")
)

while True:
    query = input('User:')
    if query.strip().lower() == "exit":
        break
    response = llm.invoke([("user", query)])
    print("AI",response.content)