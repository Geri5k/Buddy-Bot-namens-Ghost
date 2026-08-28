#                                   Imports
from google import genai
from groq import Groq
import os
from dotenv import load_dotenv
#                                   Conection Test
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

#                                            Conection of the two clients
nutzfrage = input("Deine eingabe: ")

#                                                   Groq Client
groq_client = Groq(api_key=groq_key)

def frage_groq(frage):
    antwort_groq = groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": frage }]
    )
    return antwort_groq.choices[0].message.content

ergebniss_groq = frage_groq(nutzfrage)
print(ergebniss_groq)


#                                                Gemini Client
gemini_client = genai.Client(api_key=gemini_key)

def frage_gemini(frage):
    antwort_gemini = gemini_client.models.generate_content(
        model="gemini-3.6-flash",
        contents=frage
    )
    return antwort_gemini.text

ergebniss_gemini = frage_gemini(nutzfrage)
print(ergebniss_gemini)

#                                       Conection Prompt
zusammenfassung_prompt = f"Fasse diese zwei Antworten zusammen: 1) {ergebniss_groq} 2) {ergebniss_gemini}"

antwort_zusammenfassung = frage_groq(zusammenfassung_prompt)
print(antwort_zusammenfassung)