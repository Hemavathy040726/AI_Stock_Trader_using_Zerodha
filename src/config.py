
# src/config.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Fetch API key and model name
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_LLM_MODEL = os.getenv("GROQ_LLM_MODEL", "llama-3.3-70b-versatile")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Please set it in your .env file.")


ZERODHA_API_KEY = os.getenv("ZERODHA_API_KEY")
ZERODHA_SECRET_KEY = os.getenv("ZERODHA_SECRET_KEY")
REQUEST_TOKEN_FROM_URL = os.getenv("REQUEST_TOKEN_FROM_URL")
ZERODHA_ACCESS_TOKEN= os.getenv("ZERODHA_ACCESS_TOKEN")



# Initialize Groq LLM client
llm_client = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_LLM_MODEL,
    temperature=0.5,   # You can adjust this later
)
print(f"✅ LLM initialized with model: {GROQ_LLM_MODEL}")
