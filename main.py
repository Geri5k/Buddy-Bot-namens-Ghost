#                                   API key test
import os
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

if groq_key is None: 
    print("Groq is not set")
else: 
    print("Groq is loaded")


if gemini_key is None: 
    print("Gemini is not set")
else: 
    print("Gemini is loaded")

#                                    Groq Client
from groq import Groq

client = Groq(api_key=groq_key)

antwort = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "Where is Vienna?" }]
)

print(antwort.choices[0].message.content)