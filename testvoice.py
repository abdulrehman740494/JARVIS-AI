import pyttsx3

engine = pyttsx3.init()

engine.setProperty('voice', engine.getProperty('voices')[1].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

print("Speaking now...")

engine.say("Hello Abdul Rehman. Jarvis is online.")
engine.runAndWait()

print("Done")