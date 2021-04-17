import pyautogui
import time
import keyboard
import sys

exit=False


#rows of piano tiles

pixels = [

    {'x': 360, 'y': 390, 'id': 1},
    {'x': 440, 'y': 390, 'id': 2},
    {'x': 500, 'y': 390, 'id': 3},
    {'x': 570, 'y': 390, 'id': 4},
]

def on_press(keyEvent):
    global exit
    if keyEvent.name=='esc':
        exit=True

keyboard.on_press(callback=on_press)



while(not exit):
    im = pyautogui.screenshot()
    for pixel in pixels:
        if im.getpixel((pixel['x'], pixel['y'])) == (0, 0, 0):
            print(pixel['id'])
            pyautogui.mouseDown(x=pixel['x'], y=pixel['y'])
            pyautogui.mouseUp(x=pixel['x'], y=pixel['y'])

            