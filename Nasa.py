import requests
import os
import random
from PIL import Image
import pyttsx3
from datetime import datetime 

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voice', voices[1].id) 

def speak(audio):
    Assistant.say(audio) 
    Assistant.runAndWait()

Api_key = "XY009fhg9OlHcs2EGlk2Z2KtKWMinUh3Mgim5gzQ"

def Nasanews(date):
    speak("Extracting data from nasa")
    url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key) 

    params = {'date':str(date)}

    r = requests.get(url, params=params)

    Data = r.json()

    print(Data)
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']

    Image_r = requests.get(Image_Url) 

    FileName = str(date) + ".jpg" 
    with open(FileName,'wb') as f:
        f.write(Image_r.content)

    Path_1 = "F:\\Jarvis Ai 2.0\\"+str(FileName) 

    Path_2 = "F:\\Jarvis Ai 2.0\\Nasa Data\\"+str(FileName) 

    os.rename(Path_1,Path_2)

    image = Image.open(Path_2)
    image.show() 

    speak(f"Title: {Title}")
    speak(f"According to nasa: {Info}")

def Summary(Body):
    list__ = ('1','2','3')

    value = random.choice(list__)
    path = 'F:\\Jarvis Ai 2.0\\Images Used\\'+str(value)+".jpg" 

    os.startfile(path) 

    name = str(Body)

    url = "https://hubblesite.org/api/v3/glossary/"+str(name) 

    r = requests.get(url)

    Data = r.json()

    if len(Data) != 0:
        retur = Data['definition']
        speak(f"According to nasa: {retur}") 

    else:
        speak("No data available!, Please try again!")

def MarsImage():
    name = 'curiosity'
    date = '2020-12-3'
    Api = str(Api_key)

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_key}"

    r = requests.get(url)

    Data = r.json()
    Photos = Data['photos'][:5] 

    try:
        for index, photo in enumerate(Photos):
            camera = photo['camera']
            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f"{index}.jpg"
            with open(img, 'wb') as file:
                file.write(p.content) 

            Path_1 = "F:\\Jarvis Ai 2.0\\"+str(img) 
            Path_2 =  "F:\\Jarvis Ai 2.0\\Mars Data\\"+str(img)  

            os.rename(Path_1, Path_2)
            os.startfile(Path_2)

            speak(f"Thia image was captured with {full_camera_name}")
            speak(f"This image was captured on {date_of_photo}") 

    except:
        speak('There was an error') 

def Asteroid(sdate, edate):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={sdate}&end_date={edate}&api_key={Api_key}"

    r = requests.get(url)

    Data = r.json()
    Total_astro = Data['element_count']

    neo = Data['near_earth_objects']
    speak(f"Total asteroid count detected between {sdate} and {edate} is {Total_astro}!")  
    speak("Data for the asteroids is listed below!")  

    for body in neo[sdate]:
        id = body['id']
        name = body['name']
        absolute = body['absolute_magnitude_h'] 

        print(id,name,absolute) 

def SolarSystem(planet):
    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    r = requests.get(url)
    Data = r.json()

    bodies = Data['bodies']

    Number = len(bodies)
 

    url_2 = f"https://api.le-systeme-solaire.net/rest/bodies/{planet}" 

    rrr = requests.get(url_2)

    data_2 = rrr.json() 

    mass = data_2['mass']['massValue']
    volume = data_2['vol']['volValue'] 
    density = data_2['density']
    gravity = data_2['gravity']
    escape = data_2['escape'] 

    print(f"\n{planet} has a mass of {mass} kg.\n It's volume is {volume} m3.\n It has a density of {density}  grams per cubic centimetre.\n It's gravity is {gravity} N/kg .\n It has an escape velocity of {escape} m/s.") 

    speak(f"{planet} has a mass of {mass}kg. It's volume is {volume} meters per cubic square. it has a density of {density}  grams per cubic centimetre. It's gravity is {gravity} newtons per kilogram . It has an escape velocity of {escape}  meters per second.")   

