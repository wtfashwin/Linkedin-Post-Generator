from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable not found.")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-70b-versatile")

if __name__ == "__main__":
    res = llm.invoke("what's the us currency")
    print(res)