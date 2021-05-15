import pyttsx3
engine = pyttsx3.init()
speech = input("Say Something : ")
speech1 = input("Say Something : ")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say(speech)
engine.say(speech1)
engine.runAndWait()
