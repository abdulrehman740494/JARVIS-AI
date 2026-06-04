import speech_recognition as sr
import os
import webbrowser
import datetime
import ollama
import pyttsx3
import time

engine = pyttsx3.init()

print("YOUR DESKTOP ASSISTANT JARVIS AI")
engine.runAndWait()


chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
chatStr = ""

def chat(query):

    response = ollama.chat(
        model="gemma3:1b",
        keep_alive="10m",
        messages=[
            {
                "role": "system",
                "content": """
You are Jarvis, a helpful voice assistant.
Rules:
- Always reply in English only
- Never say you are Gemma or any other AI
- Never use other languages
- Keep answers short (1-2 lines)
"""
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    answer = response["message"]["content"].strip()

    print("Jarvis:", answer)

    say(answer)

    return answer

def ai(prompt):
    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    text = response["message"]["content"]

    print(text)

    with open("Openai/response.txt", "w", encoding="utf-8") as f:
        f.write(text)


def say(text):
    print("Jarvis:", text)

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 190)

    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)
    engine.stop()

    print("Finished Speaking")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(
            source,
            timeout=5,
            phrase_time_limit=8
        )

        try:
            print("Recognizing...")

            query = r.recognize_google(
                audio,
                language="en-US"
            )

            print(f"User said: {query}")

            return query

        except Exception:
            return None


if __name__ == '__main__':
    say("HELLO SIR JARVIS HERE , HOW CAN I HELP YOU?")
    while True:
        query = takeCommand()

        if not query:
            continue
        # todo: Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        # todo: Add a feature to play a specific song
        if "play music" in query.lower():
            musicPath = r"C:\Users\wajiz.pk\Downloads\music.mp3"
            os.startfile(musicPath)

        elif "the time" in query:
            musicPath = "/Users/wajiz.pk/Downloads/downfall-21371.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour}  {min} minutes")

        elif "open pass".lower() in query.lower():
            os.system(f"open /Applications/Passky.app")

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        else:
            print("Chatting...")

            response = chat(query)

            print("Response received")
        # say(query)