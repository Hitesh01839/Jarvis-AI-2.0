import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import requests
import wikipedia
import time
from time import sleep
import pyautogui as pg
from pyautogui import hotkey, click 
from pytube import YouTube
import pyperclip
import keyboard 
import pyjokes
import wolframalpha
from PyDictionary import PyDictionary as Diction 
import datetime
from googletrans import Translator
from playsound import playsound
import pywikihow
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import random
import chatbot
from geopy.distance import great_circle
from geopy.geocoders import Nominatim 
import geocoder


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

def search(topic: str): 
    """Searches about the topic on Google"""
    link = 'https://www.google.com/search?q={}'.format(topic)
    webbrowser.open(link)

def to_play_video_on_yt(topic): 
    """This will play a video on youtube of the input topic"""  
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        raise Exception("No video found.")
    
    #print("Videos found, opening most recent video")
    webbrowser.open("https://www.youtube.com"+lst[count-5])
    return "https://www.youtube.com"+lst[count-5] 

def screenshot():
    try:
        img = pg.screenshot()
        sait = time.time() 
        img.save(f"F:\\jarvis screenshots\\img{sait}.jpg")   
        os.startfile(f"F:\\jarvis screenshots\\img{sait}.jpg")
        speak("Screenshot has been taken sir!")
        img.show() 
    except Exception as e:
        speak("Screenshot was not taken") 

def takeTel():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("say anything: ") 
        r.pause_threshold = 1
        audio= r.listen(source)
        try:
            query = r.recognize_google(audio, language='te')
            print(query)
        except:
            print("sorry, could not recognise") 
            return "None" 
    return query.lower() 

def Translate():
    speak("Tell me the line")
    line = takeTel()
    translate = Translator()
    result = translate.translate(line)
    Text = result.text
    speak(f"The translation for this is {Text}") 

def speedTestStart():
    os.startfile('F:\\Jarvis Ai 2.0\\speedTestInternet.py')

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

def Dict():
    speak("Tell me the problem")
    probl = takeCommand()

    if 'meaning' in probl:
        probl = probl.replace("what is the" "")
        probl = probl.replace("jarvis", "")
        probl = probl.replace("of", "")
        probl = probl.replace("meaning of", "")
        result = Diction.meaning(probl) 
        speak(f"The meaning for {probl} is {result}") 

    elif 'synonym' in probl:
        probl = probl.replace("what is the" "")
        probl = probl.replace("jarvis", "")
        probl = probl.replace("of", "")
        probl = probl.replace("synonym of", "")
        result = Diction.synonym(probl) 
        speak(f"The synonym for {probl} is {result}")          
    
    elif 'antonym' in probl:
        probl = probl.replace("what is the" "")
        probl = probl.replace("jarvis", "")
        probl = probl.replace("of", "")
        probl = probl.replace("antonym of", "") 
        result = Diction.antonym(probl) 
        speak(f"The antonym for {probl} is {result}")          

def youtubeVidDownload():
    sleep(3)
    click(x=676,y=50) 
    value = hotkey('ctrl', 'c')
    value = pyperclip.paste()

    Link = str(value)
    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('F:\\Jarvis Ai 2.0\\Youtube videos download\\') 
    Download(Link) 
    speak("The Video has been downloaded!") 

def YoutubeAuto():
    speak('What is command')
    comm = takeCommand()

    if 'pause' in comm:
        keyboard.press('space bar')
    
    if 'resume' in comm:
        keyboard.press('space bar')
    
    elif 'start again' in comm:
        keyboard.press('0')

    elif 'mute video' in comm:
        keyboard.press('m')
    
    elif 'skip' in comm:
        keyboard.press('l')
    
    elif 'backward' in comm:
        keyboard.press('j')
   
    elif 'full screen' in comm:
        keyboard.press('f')
 
def wolframAlpha(query) :
    api_key = "ERVX84-K8VH2H9PE2"
    requester = wolframAlpha.Client(api_key)
    requested = requester.query(query)


    try:
        answer = next(requested.results).text()
        return answer
    except:
        speak("String value not iterable")

def Calculator(query):
    Term = str(query)

    Term = Term.replace("jarvis","")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divided by","/")
    Term = Term.replace("multiplied by","*")

    Final = str(Term)
    try:
        result = wolframAlpha(Final)
        speak(f"{result}")
    except: 
        speak("String value not iterable")

def DateConverter(date):
    Date = date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace(" ","") 
    return str(Date) 

def My_Location():
    ipAdd = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
    op = "https://www.google.com/maps/@17.439673,78.4865596,15z"

    speak("Checking...")

    webbrowser.open(op) 

    geo_requests = requests.get(url)
    geo_data = geo_requests.json()  

    city = geo_data['city']
    country = geo_data['country']   
    speak(f"You are now in {city, country}") 

def GoogleMaps(place):
    url_place = "https://www.google.com/maps/place/"+str(place) 

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(place, addressdetails=True)
    target_latlon = location.latitude, location.longitude
    location = location.raw['address']

    target = {'city' : location.get('city',''), 'state' : location.get('state',''), 'country' : location.get('country','')} 
    current_location = geocoder.ip('me')
    current_lation = current_location.latlng 

    distance = str(great_circle(current_lation, target_latlon))
    distance = str(distance.split(' ', 1)[0])

    distance = round(float(distance), 2)
    
    webbrowser.open(url=url_place)

    print(target)
    speak(target) 
    speak(f"Sir, {place} is {distance} Kilometeres away from you!")  

def Notepad():
    speak("Say what is the note sir!")

    write1 = takeCommand()
    time = datetime.datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"
    with open(filename, 'w') as file:
        file.write(write1) 

    path1 = "F:\\Jarvis Ai 2.0\\" + str(filename)
    path2 = "F:\\Jarvis Ai 2.0\\Notepad\\" + str(filename) 

    os.rename(path1,path2)
    os.startfile(path2)


def taskExe():

    speak("Allow me to introduce myself!. I am Jarvis a virtual Artificial intelligence, and i am here to assist you with a variety of tasks as best as i can. twenty four hours a day, seven days a week, importing all preferences from home interface! system is now fullly operational.") 

    def Music():
        speak("Playing songs")
        os.startfile('F:\\songs') 
   
    while True:
        query = takeCommand()

        if 'hello' in query:
            speak("Hello sir!")
            speak("How may i help you")

        elif 'how are you' in query:
            speak("I am fine sir, what about you?")

        elif "you need a break" in query:
            speak("Ok sir, call me anytime")
            break
        
        elif "exit" in query:
            speak("Ok sir, call me anytime")
            break

        elif "bye" in query:
            speak("bye sir")
            break

        elif 'search youtube' in query:
            speak("Ok sir, This is what i found on youtube")
            query = query.replace('jarvis', "")
            query = query.replace('search youtube', "") 
            query = query.replace('for', "")  
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web) 
            to_play_video_on_yt(web) 
        
        elif 'open youtube' in query:
            speak("Ok sir, This is what i found on youtube")
            query = query.replace("jarvis","")
            query = query.replace("open youtube","")
            query = query.replace("and","")
            query = query.replace("play","") 
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web) 
            to_play_video_on_yt(web) 

        elif "search for" in query:
            speak("This is what i found for your, search sir!")
            query = query.replace('jarvis', "") 
            query = query.replace('search for', "") 
            # search(query)

            try:
                search = wikipedia.summary(query,2)
                speak(search) 

            except:
                speak("None found")  

        elif 'website' in query:
            speak('Ok sir! ')
            query = query.replace('jarvis', "")
            query = query.replace('website', "")
            query = query.replace(" ", "") 
            web1 = query.replace('open', "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched!") 

        elif 'launch' in query:
            speak("What is the name of the website!")
            name = takeCommand()
            web = 'https://www.'+name+'.com'
            webbrowser.open(web)

        elif 'music' in query:
            Music()

        elif 'play songs' in query:
            name = takeCommand()
            songs = random.choice(["On and on", "Astrounaut in the ocean", "Dance Monkey", "Closer"])
            to_play_video_on_yt(songs) 
        
        elif 'play some songs' in query:
            name = takeCommand()
            songs = random.choice(["On and on", "Astrounaut in the ocean", "Dance Monkey", "Closer"]) 
            to_play_video_on_yt(songs) 
       
        elif 'play some music' in query:
            name = takeCommand()
            songs = random.choice(["On and on", "Astrounaut in the ocean", "Dance Monkey", "Closer"]) 
            to_play_video_on_yt(songs) 

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('jarvis', "")
            query = query.replace('wikipedia', "")
            query = query.replace('search', "")
            wiki = wikipedia.summary(query, 2)
            speak(f"AAccording to wikipedia: {wiki}") 

        elif 'send a message' in query:
            name = query.replace("send message","") 
            name = name.replace("to","") 
            name = name.replace("a","") 
            name = name.replace("message","") 
            Name = str(name)
            speak(f"What is the message to send {Name}")
            Msg = takeCommand()
            from watsappAutomation import whatsMsg 
            whatsMsg(Name, Msg)  
        
        elif 'send message' in query:
            name = query.replace("send message","") 
            name = name.replace("to","") 
            name = name.replace("a","") 
            name = name.replace("message","") 
            Name = str(name)
            speak(f"What is the message to send {Name}")
            Msg = takeCommand()
            from watsappAutomation import whatsMsg
            whatsMsg(Name, Msg)  

        elif 'call' in query:
            from watsappAutomation import whatsCall
            name = query.replace("call","")
            name = name.replace("jarvis","")
            Name = str(name)
            whatsCall(Name) 
        
        elif 'video call' in query:
            from watsappAutomation import whatsVideoCall
            name = query.replace("call","")
            name = name.replace("jarvis","")
            name = name.replace("video","")
            name = name.replace("to","") 
            Name = str(name)
            whatsVideoCall(Name)  

        elif 'show chat' in query:
            speak("What is the person name")
            name = takeCommand()
            from watsappAutomation import whatsAppChat
            whatsAppChat(name) 

        elif 'screenshot' in query:
            screenshot() 

        elif 'open zoom' in query: 
            print("Opening Zoom...")
            speak("Opening Zoom...")
            codePath = "C:\\Users\\New\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codePath)
        
        elif 'join class' in query:
            import zoom_bot
            os.startfile('zoom_bot.py') 
        
        elif 'join a class' in query:
            import zoom_bot
            os.startfile('zoom_bot.py') 
        
        elif 'join a meeting' in query:
            import zoom_bot
            os.startfile('zoom_bot.py') 
            
        elif 'code' in query:
            cpath = "C:\\Users\\New\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(cpath)

        elif 'open discord' in query:
            dipath = "C:\\Users\\New\\AppData\\Local\\Discord\\Update.exe" 
            os.startfile(dipath) 

        elif 'open OBS' in query:
            obspath = "D:\\obs-studio\\bin\\64bit\\obs64.exe"
            os.startfile(obspath)

        elif 'open game loop' in query:
            gameloopath = "D:\\Program Files\\TxGameAssistant\\AppMarket\\AppMarket.exe"
            os.startfile(gameloopath)

        elif 'open epic games' in query:
            epicpath = "D:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(epicpath)

        elif 'vpn' in query:
            vpnpath = "C:\\Program Files (x86)\\TAP-ProtonVPN\\ProtonVPN.exe"
            os.startfile(vpnpath)

        elif 'open command prompt' in query:
            os.system('start cmd')

        elif "switch window" in query:
            pg.keyDown("alt")
            pg.press("tab")
            time.sleep(2)
            pg.keyUp("alt")

        elif 'jarvis you there' in query:
            speak("at your service sir!.") 
        
        elif 'jarvis are you there' in query:
            speak("at your service sir!.") 
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')
        
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/') 

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@21.125498,81.914063,5z') 

        elif "close notepad" in query:
            speak("Okay sir!. Closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'close zoom' in query:
            speak("Okay sir!. Closing zoom")
            os.system("taskkill /f /im Zoom.exe")

        elif 'close discord' in query:
            speak("Okay sir!. Closing discord")
            os.system("taskkill /f /im Discord.exe")

        elif 'close VPN' in query:
            speak("Okay sir!. Closing vpn")
            os.system("taskkill /f /im ProtonVPN.exe")

        elif 'close epic games' in query:
            speak("Okay sir!. Closing epic games")
            os.system("taskkill /f /im EpicGamesLauncher.exe")

        elif 'close obs ' in query:
            speak("Okay sir!. Closing obs")
            os.system("taskkill /f /im obs64.exe")

        elif 'close gameloop' in query:
            speak("Okay sir!. Closing gameloop")
            os.system("taskkill /f /im AppMarket.exe.exe")

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'resume' in query:
            keyboard.press('space bar')

        elif 'start again' in query:
            keyboard.press('0')

        elif 'mute video' in query:
            keyboard.press('m')
        
        elif 'skip' in query:
            keyboard.press('l')
        
        elif 'backward' in query:
            keyboard.press('j')
    
        elif 'full screen' in query:
            keyboard.press('f')

        elif 'youtube tools' in query:
            YoutubeAuto()
        
        elif 'disable youtube tools' in query:
            speak("Disabled youtube tools!")

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
        
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        
        elif 'open new chrome window' in query:
            keyboard.press_and_release('ctrl + n')
        
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h') 
        
        elif 'incognito' in query:
            keyboard.press_and_release('Ctrl+Shift+n') 

        elif 'joke' in query:
            get=pyjokes.get_joke()
            speak(get) 

        elif 'repeat my words' in query:
            speak("Speak sir!")
            jj = takeCommand()
            speak(f"You said: {jj}") 

        elif 'dictionary' in query:
            Dict() 

        elif 'alarm' in query:
            speak("Enter the time")
            os.startfile('F:\\Jarvis Ai 2.0\\Alarm.py')
            # speak("Alarm done") 

        elif 'translator' in query:
            Translate() 
        
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that", "")
            rememberMsg = rememberMsg.replace("jarvis", "") 
            remember = open('remember.txt','w')
            remember.write(rememberMsg)
            remember.close() 

        elif 'what do you remember' in query:
            remember = open('remember.txt', 'r')
            speak(f"You told me to remember that {remember.read()}")  

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("This is what i found!")
            # search(query)

            try:
                search = wikipedia.summary(query,2)
                speak(search) 

            except:
                speak("None found")  
        
        elif 'what are' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis", "")
            query = query.replace("what are", "")
            query = query.replace("google", "")
            speak("This is what i found!")
            search(query)

            try:
                max_result = 1
                how_to_func1 = search_wikihow(query=query,max_results=max_result)
                assert len(how_to_func1) == 1
                how_to_func1[0].print()
                speak(how_to_func1[0].summary)

            except:
                speak("None found") 
                
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            print(f"Your IP address is {ip}")
            speak(f"your ip address is {ip}")  

        elif 'weather' in query:
            temperature_jarvis()

        elif 'temperature' in query:
            temperature_jarvis()
        
        elif 'bored' in query:
            speak("What do you want me to do sir") 

        elif 'no thanks' in query:
            speak("Ok sir!")

        elif 'how to' in query:
            speak('Searching the internet')
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = pywikihow.search_wikihow(op,max_result) 
            assert len(how_to_func) == 1 
            how_to_func[0].print()
            speak(how_to_func[0].summary)  

        elif 'who are you' in query:
            speak_words_for_who_are_you = ["I am Jarvis. Mister Hetesh's personnel assistant!",
                                           "I am Jarvis. Mister Hetesh is my boss!", "I am Jarvis.I work for Mister Hetesh!"]  
            words_to_speak_who_are_you = random.choice( 
                speak_words_for_who_are_you)
            speak(words_to_speak_who_are_you) 

        elif 'what are you' in query:
            speak("Allow me to introduce myself!. I am Jarvis a virtual Artificial intelligence, and i am here to assist you with a variety of tasks as best as i can. twenty four hours a day, seven days a week")  
        
        elif 'download' in query:
            youtubeVidDownload()

        elif 'internet speed' in query:
            speedTestStart() 

        elif 'wolfram alpha' in query:
            wolframAlpha()

        elif 'plus' in query:
            Calculator()

        elif 'minus' in query:
            Calculator()

        elif 'divided' in query:
            Calculator()

        elif 'thank you' in query:
            speak("Anytime sir") 

        elif 'multiplied' in query:
            Calculator()
        
        elif 'space news' in query:
            speak("Which date news do you want to know about")
            Date = takeCommand()

            Value = DateConverter(Date)

            from Nasa import Nasanews
            Nasanews(Value) 

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            query = query.replace("tell ","")
            query = query.replace("me ","")  
            Summary(query)

        elif 'mars image' in query:
            from Nasa import MarsImage
            MarsImage() 

        elif 'near earth objects' in query:
            from Nasa import Asteroid

            speak("Enter the date sir!")
            start = input("Enter the start date: \n")
            end = input("Enter the end date: \n") 
            Asteroid(start, end)
        
        elif 'asteroid' in query:
            from Nasa import Asteroid

            speak("Enter the date sir!")
            start = input("Enter the start date: \n")
            end = input("Enter the end date: \n") 
            Asteroid(start, end)

        elif 'solar system' in query:
            from Nasa import SolarSystem

            speak("Tell the name of the object!")
            bod = takeCommand()
            body = bod.replace(" ","")
            body = body.replace(" ","")
            Body = str(body)
            SolarSystem(planet=Body) 

        elif 'where am i' in query:
            My_Location()
        
        elif 'my location' in query:
            My_Location()
        
        elif 'track me' in query:
            My_Location()

        elif 'where is' in query:
            Place = query.replace("where is","")
            Place = Place.replace("jarvis","")
            GoogleMaps(Place) 

        elif 'make a note' in query:
            Notepad()
        
        elif 'write a note' in query:
            Notepad()
        
        elif 'note this' in query:
            Notepad()

        else:
            reply = chatbot.ChatterBot(query)
            speak(reply) 

taskExe() 
