from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep 
import pyautogui as pg
from pyautogui import pyscreeze

def whatsMsg(name,message):

    startfile("C:\\ProgramData\\New\\WhatsApp\\WhatsApp.exe")
    sleep(5) 
    kk = pg.locateOnScreen("search.png")
    while True:
        if kk != None:
            pg.click(kk) 
            pg.write(name)
            sleep(3) 
            pg.moveRel(0, +150)
            pg.click() 
            sleep(2)  
            hh = pg.locateOnScreen("text.png") 
            pg.click(hh) 
            pg.write(message)
            pg.press('enter') 
            break 

def whatsCall(name):
    startfile("C:\\ProgramData\\New\\WhatsApp\\WhatsApp.exe")
    sleep(25) 
    kk = pg.locateOnScreen("search.png")
    while True:
        if kk != None:
            pg.click(kk) 
            pg.write(name)
            sleep(3) 
            pg.moveRel(0, +150)
            pg.click() 
            sleep(2) 
            hh = pg.locateOnScreen("call.png")
            pg.click(hh) 
            break

def whatsVideoCall(name):
    startfile("C:\\ProgramData\\New\\WhatsApp\\WhatsApp.exe")
    sleep(25) 
    kk = pg.locateOnScreen("search.png")
    while True:
        if kk != None:
            pg.click(kk) 
            pg.write(name)
            sleep(3) 
            pg.moveRel(0, +150)
            pg.click() 
            sleep(2) 
            hh = pg.locateOnScreen("VideoCall.png") 
            pg.click(hh) 
            break  

def whatsAppChat(name):
    startfile("C:\\ProgramData\\New\\WhatsApp\\WhatsApp.exe")
    sleep(25) 
    kk = pg.locateOnScreen("search.png")
    while True:
        if kk != None:
            pg.click(kk) 
            pg.write(name)
            sleep(3) 
            pg.moveRel(0, +150)
            pg.click() 
            sleep(2) 
            hh = pg.locateOnScreen("text.png") 
            pg.click(hh)  
            break  

