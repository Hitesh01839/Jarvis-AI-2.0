from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep 
import pyautogui as pg
from pyautogui import pyscreeze 
import pyperclip 
import random 

startfile("C:\\ProgramData\\New\\WhatsApp\\WhatsApp.exe") 
sleep(5) 
position1 = pg.locateOnScreen("./smily_paper.png", confidence=.6)
x = position1[0]
y = position1[1]

def get_message():
    global x, y

    position = pg.locateOnScreen("./smily_paper.png", confidence=.6)
    x = position1[0]
    y = position1[1] 
    pg.moveTo(x,y)
    pg.moveTo(x + 73, y - 60)
    pg.tripleClick()
    pg.rightClick() 
    pg.moveRel(12,15) 
    pg.click() 
    watsapp_message = pyperclip.paste() 
    pg.click() 
    print("Message Recieved: " + watsapp_message)

    return watsapp_message

def post_respose(message):
    global x, y 

    position = pg.locateOnScreen("./smily_paper.png", confidence=.6)
    x = position1[0]
    y = position1[1] 
    hh = pg.locateOnScreen("text.png") 
    pg.click(hh) 
    pg.typewrite(message, interval=.01)
    pg.press('enter') 

def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    else:
        if random_no == 0:
            return "Thats cool!"
        elif random_no == 1:
            reply = ["Yaa", "I know", "Haa", "What to do"]
            ran = random.choice(reply)
            return ran
        else:
            return "I want to eat something" 

    
def check_for_new_messages():
    pg.moveTo(x+75, y-40) 

    while True:
        try:
            position = pg.locateOnScreen("reen_dot.png", confidence=.7)

            if position is not None:
                pg.moveTo(position)
                pg.moveRel(-100, 0) 
                pg.click()
                sleep(.5) 
                print("is green") 
                processed_message = process_response(get_message())
                post_respose(processed_message)

        except:
            print("No new messages yet...")
        sleep(5)  


check_for_new_messages() 
