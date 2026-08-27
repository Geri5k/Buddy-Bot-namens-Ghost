import os
from dotenv import load_dotenv

load_dotenv()

groq = os.getenv("GROQ_API_KEY")
gemini = os.getenv("GEMINI_API_KEY")

if groq is None: print("Groq is not set")
else: print("Groq is loaded")


if gemini is None: print("Gemini is not set")
else: print("Gemini is loaded")
