import pyautogui as pg
from pyautogui import locateOnScreen
import subprocess
import datetime
import time

def join_meeting():
    id1 = input("Enter the meeting id: ")
    password = input("Enter the meeting password: ") 
    subprocess.call("C:\\Users\\New\\AppData\\Roaming\\Zoom\\bin_00\\Zoom.exe")  

    while True:
        time.sleep(5)
        pg.click(x=433, y=271) 
        time.sleep(2) 
        pg.click(x=672, y=324) 
        pg.write(id1)
        pg.press('enter') 
        pg.click(x=759, y=313)
        time.sleep(3) 
        pg.write(password) 
        pg.press('enter')
        break 
    # sys.exit() 

join_meeting() 