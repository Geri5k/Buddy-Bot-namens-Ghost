#                                   Imports
from google import genai
from google.genai import errors
from groq import Groq
import groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

#                                                        The Core
groq_client = Groq(api_key=groq_key)
gemini_client = genai.Client(api_key=gemini_key)


    #                                                   Groq Client

def frage_groq(frage):
    antwort_groq = groq_client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": frage }]
    )
    return antwort_groq.choices[0].message.content

    #                                                Gemini Client

def frage_gemini(frage):
    antwort_gemini = gemini_client.models.generate_content(
        model="gemini-3.6-flash",
        contents=frage
    )
    return antwort_gemini.text

#                                                       Greeting
print("Heyo, was gehen wir Heute an? (Zum Beenden tippe: exit, Weitere Befehle: befehle)")

#                                                       Memory
verlauf = []

     #                                            The Task
while True: 
    print("-" * 40)   
    nutzfrage = input("Deine eingabe: ")
    if nutzfrage == "exit": break

    if nutzfrage == "befehle":
        print("Verlauf anzeigen: verlauf\nVerlauf löschen: löschen")
        continue

    if nutzfrage == "löschen":
        verlauf = []
        print("Verlauf wurde gelöscht.")
        continue

    if nutzfrage == "verlauf": 
        for verlauf_item in verlauf:
            print("-" * 40)
            print(verlauf_item)
        continue 

    kontext_frage = f"Bisheriger Gesprächsverlauf:\n{'\n'.join(verlauf)}\n\nNeue Frage: {nutzfrage}"

    try:
        ergebniss_groq = frage_groq(kontext_frage)
    except groq.APIError:
        ergebniss_groq = None

    try:
        ergebniss_gemini = frage_gemini(kontext_frage)
    except errors.ServerError:
        ergebniss_gemini = None

    #                                       Conection Prompt
    if ergebniss_groq is not None and ergebniss_gemini is not None:
        zusammenfassung_prompt = f"Fasse diese zwei Antworten zusammen: 1) {ergebniss_groq} 2) {ergebniss_gemini}"
        antwort_zusammenfassung = frage_groq(zusammenfassung_prompt)
        print("-" * 40)
        bot_antwort = (f"Ghost sagt: {antwort_zusammenfassung}")

    elif ergebniss_groq is not None and ergebniss_gemini is None:
        print("-" * 40)
        bot_antwort = (f"Ghost sagt: Gemini ist ausgefallen. Hier ist die Antwort von Groq: {ergebniss_groq}")

    elif ergebniss_groq is None and ergebniss_gemini is not None:
        print("-" * 40)
        bot_antwort = (f"Ghost sagt: Groq ist ausgefallen. Hier ist die Antwort von Gemini: {ergebniss_gemini}")

    else:
        print("-" * 40)
        bot_antwort = (f"Ghost sagt: Sorry, beide KIs sind gerade nicht erreichbar, versuch´s später nochmal.")

    print(bot_antwort)
#                                   Conection to Memory
    verlauf.append(f"Nutzer: {nutzfrage}\nGhost: {bot_antwort}")