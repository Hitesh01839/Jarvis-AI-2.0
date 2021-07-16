import datetime
import playsound
import pyttsx3
import speech_recognition as sr 
from bs4 import BeautifulSoup
import requests
import time


time = input("Enter the time: \n")

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voice', voices[0].id) 

def speak(audio):
    Assistant.say(audio) 
    Assistant.runAndWait() 
 
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
            # return "none"  
    return query.lower() 

def temperature_jarvis(): 
    ipAdd = requests.get('https://api.ipify.org').text
    # print(ipAdd) 
    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    city = geo_data['city'] 
    # print(city) 
    search_of_temperature = f"temperature of {city}" 
    url = f"https://www.google.com/search?q={search_of_temperature}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text 
    data_found = temp 
    speak(f"Sir the current temperature of {city} is {data_found}")

while True:
    
    Time_Ac = datetime.datetime.now()
    now = Time_Ac.strftime("%H:%M:%S")

    if now == time:
        playsound.playsound('ironman.mp3')
        # time.sleep(26) 
        speak("Wke Up! sir!") 
        temperature_jarvis() 
        kk = datetime.datetime.now().strftime("%H:%M")
        speak(f"Sir it is already {kk}!")   
        query = takeCommand()
        if "wait" in query:
            speak("Please wake up! sir!") 
        else:
            speak("Please wake up! sir!") 
    elif now>time:
        break 