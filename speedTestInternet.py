import pyttsx3

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voice', voices[1].id) 

def speak(audio):
    Assistant.say(audio) 
    Assistant.runAndWait() 


def speedTest():
    speak("Checking speed...")
    import speedtest
    speed = speedtest.Speedtest()   
    upload = speed.upload()
    correct_up = int(int(upload)/800000)
    download = speed.download()
    correct_down = int(int(download)/800000)

    speak(f"Doownloading speed is {correct_down} mb per second")
    speak(f"Uploading speed is {correct_up} mb per second")
    # exit() 