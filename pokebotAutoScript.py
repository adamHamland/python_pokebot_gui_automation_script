#written by Adam Hamilton-Sutherland

#This is a work in progress. Script only works in 1920x1080 screens 
#when the discord window occupys the left half of the screen. 
#This is because of how the mouse input works.

import random
import time
import pynput
import signal
import os

#from pynput.keyboard import Key, Controller

from pynput.mouse import Button, Controller
from pynput import keyboard
import clipboard

#keyboard = pynput.keyboard.Controller() 

mouse = pynput.mouse.Controller()
    
def gameLoop():
    delay = random.randrange(10,12)

    time.sleep(delay)

    keyboard.Controller().type(';p')
    
    time.sleep(1)
    
    keyboard.Controller().press(keyboard.Key.enter)
    keyboard.Controller().release(keyboard.Key.enter)

    time.sleep(3)

    copyMsg()

    poke = readClipboard()

    if poke == '':
        exit()
    else:
        delay = random.randrange(1,2)
        time.sleep(delay)

        keyboard.Controller().type(poke)

        time.sleep(1)

        keyboard.Controller().press(keyboard.Key.enter)
        keyboard.Controller().release(keyboard.Key.enter)


def copyMsg():
    a,b = mouse.position
    mouse.position=(a,870)

    time.sleep(.3)
    
    mouse.press(Button.left)
    time.sleep(.1)
    mouse.move(0,-100)
    time.sleep(.1)
    mouse.release(Button.left)
    
    time.sleep(.5)

    keyboard.Controller().press(keyboard.Key.ctrl)
    keyboard.Controller().press('c')
    keyboard.Controller().release('c')
    keyboard.Controller().release(keyboard.Key.ctrl)

def readClipboard():
    text = clipboard.paste()
    text = clipboard.paste()

    print("---")
    print(text)
    print("---")
    
    if 'continue' in text or 'captcha' in text or 'attempts' in text or 'you there' in text or 'banned' in text or 'bot' in text:
        print("Captcha detected. Exiting...")
        return ''
    elif 'Shiny' in text:
        print("Shiny found. Throwing mb.", "\n===\n")
        return 'mb'
    elif 'Legendary' in text:
        print("Legendary found. Throwing ub.", "\n===\n")
        return 'ub'
    elif 'Super Rare' in text:
        print("Super Rare found. Throwing gb.", "\n===\n")
        return 'gb'
    elif 'Common' in text or 'Uncommon' in text or 'Rare' in text:
        print("Common, Uncommon, or Rare found. Throwing pb.", "\n===\n")
        return 'pb'
    else:
        print("Error. Exiting...")
        return ''

#threading and signal handleing
def on_press(key):
    pass

def on_release(key):
    if key == keyboard.Key.esc:
        print("Esc key pressed. Exiting...")

        signal.pthread_kill(os.getppid(), signal.SIGINT)


#main

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

for x in range(0,10): #no way this runs more than 10 times without getting the captcha

    time.sleep(10)
    
    keyboard.Controller().type(';shop buy 1 20')
    
    time.sleep(4)
    
    keyboard.Controller().press(keyboard.Key.enter)
    keyboard.Controller().release(keyboard.Key.enter)

    for x in range(0,20):
        gameLoop()
    

