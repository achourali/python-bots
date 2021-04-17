import pyautogui
import keyboard
import time
import asyncio


def moveMouse(keyEvent):
    print(keyEvent.name)
    if keyEvent.name=='droite':
        pyautogui.move(xOffset=10,yOffset=0,_pause=False)
    elif keyEvent.name=='gauche':
        pyautogui.move(xOffset=-10,yOffset=0,_pause=False)
    elif keyEvent.name=='haut':
        pyautogui.move(xOffset=0,yOffset=-10,_pause=False)
    elif keyEvent.name=='bas':
        pyautogui.move(xOffset=0,yOffset=10,_pause=False)
    elif keyEvent.name=='ctrl':
        pyautogui.mouseDown()
        pyautogui.mouseUp()
    elif keyEvent.name=='ctrl droite':
        pyautogui.rightClick()


keyboard.on_press(
    callback=moveMouse
)

while(True):
    time.sleep(5)
