"""
Groq LLM initialization and configuration (Alternative to OpenAI).
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY", "")

# Using Llama 3.3 on Groq as a free alternative to GPT-4o
llm = ChatGroq(model="llama-3.3-70b-versatile")