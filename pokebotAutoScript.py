import pynput
import random
import time

from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller

import clipboard


keyboard = pynput.keyboard.Controller() 
mouse = pynput.mouse.Controller()
    
def gameLoop():
    delay = random.randrange(10,12)

    time.sleep(delay)

    keyboard.type(';p')
    
    delay = 1
    time.sleep(delay)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    delay = 3
    time.sleep(delay)

    copyMsg()

    poke = readClipboard()

    if poke == '':
        exit()
    
    delay = random.randrange(2,4)
    time.sleep(delay)

    keyboard.type(poke)

    delay = 1
    time.sleep(delay)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def copyMsg():
    a,b = mouse.position
    mouse.position=(a,920)

    time.sleep(.3)
    
    mouse.press(Button.left)
    time.sleep(.1)
    mouse.move(0,-100)
    time.sleep(.1)
    mouse.release(Button.left)
    
    time.sleep(.5)

    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)

def readClipboard():
    text = clipboard.paste()
    
    print(text)

    if 'captcha' in text:
        return ''
    elif 'Shiny' in text:
        return 'mb'
    elif 'Legendary' in text:
        return 'ub'
    elif 'Super Rare' in text:
        return 'gb'
    else:
        return 'pb'

#main

for x in range(0,1):
    time.sleep(10)
    
    keyboard.type(';shop buy 1 20')
    
    time.sleep(4)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    for x in range(0,5):
        gameLoop()
    

