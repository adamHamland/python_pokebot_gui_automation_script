#written by Adam Hamilton-Sutherland

#This is a work in progress. Script only works in 1920x1080 screens 
#when the discord window occupys the left half of the screen. 
#This is because of how the mouse input works.

import random
import time
import pynput

from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller

import clipboard


keyboard = pynput.keyboard.Controller() 
mouse = pynput.mouse.Controller()
    
def gameLoop():
    delay = random.randrange(10,12)

    time.sleep(delay)

    keyboard.type(';p')
    
    time.sleep(1)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(3)

    copyMsg()

    poke = readClipboard()

    if poke == '':
        exit()
    else:
        delay = random.randrange(1,2)
        time.sleep(delay)

        keyboard.type(poke)

        time.sleep(1)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


def copyMsg():
    a,b = mouse.position
    mouse.position=(a,890)

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
    
    if 'captcha' in text or 'attempts' in text or 'you there' in text or 'banned' in text:
        print("Captcha detected. Exiting...")
        return ''
    elif 'Shiny' in text:
        print("Shiny found. Throwing mb.", "\n")
        return 'mb'
    elif 'Legendary' in text:
        print("Legendary found. Throwing ub.", "\n")
        return 'ub'
    elif 'Super Rare' in text:
        print("Super Rare found. Throwing gb.", "\n")
        return 'gb'
    elif 'Common' in text or 'Uncommon' in text or 'Rare' in text:
        print("Common, Uncommon, or Rare found. Throwing pb.", "\n")
        return 'pb'
    else:
        print("Error. Exiting...")
        return ''

#main

for x in range(0,10): #no way this runs more than 10 times without getting the captcha

    time.sleep(10)
    
    keyboard.type(';shop buy 1 20')
    
    time.sleep(4)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    for x in range(0,20):
        gameLoop()
    

