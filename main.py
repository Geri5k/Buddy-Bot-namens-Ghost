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

groq_client = Groq(api_key=groq_key)

antwort_groq = groq_client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": input("Deine Frage: ") }]
)

print(antwort_groq.choices[0].message.content)


#                                  Gemini Client
from google import genai

gemini_client = genai.Client(api_key=gemini_key)

antwort_gemini = gemini_client.models.generate_content(
    model="gemini-3.7-flash",
    contents=input("Deine Frage: ")
)

print(antwort_gemini.text)