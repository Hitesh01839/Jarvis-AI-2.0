import pyautogui as pg 
import time

while True:
    posXY  = pg.position()
    print(posXY, pg.pixel(posXY[0], posXY[1]))
    time.sleep(1)
    if posXY[0] == 0:
        break  
