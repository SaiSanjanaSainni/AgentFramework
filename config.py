import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Groq API Key not fount in .env")
