import speech_recognition as sr
import os

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("say anything: ") 
        r.pause_threshold = 1
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
            print(query)
        except:
            print("sorry, could not recognise") 
            return "None" 
    return query.lower() 

while True:
    wake_up = takeCommand()

    if 'wake up' in wake_up:
        os.startfile("F:\\Jarvis Ai 2.0\\jarvis.py") 

    else:
        print("Nothing...")