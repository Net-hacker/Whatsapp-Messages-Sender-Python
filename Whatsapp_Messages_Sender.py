import pywhatkit
from pynput.keyboard import Key, Controller
import time
#If you wanna remove the created .txt File let this here else remove that (not recommended)
import os

#If you wanna remove the created .txt File let this here else remove that (not recommended)
if os.path.exists('pywhatkit_dbs.txt'):
    os.remove('pywhatkit_dbs.txt' )

#The Script
keyboard = Controller()
print('Have you connected Whatsapp with Whatsapp Web. If not press ctrl + c')
time.sleep(5)
telephone = int(input('Please type the Number (without prefix and spaces): '))
message = str(input('The Message: '))
h = int(input('At what Hour the Message will sented: '))
m = int(input('At what Minute the Message will sented: '))
pywhatkit.sendwhatmsg('#Add your prefix here ' + str(telephone), message, h, m)
keyboard.press(Key.esc)
keyboard.release(Key.esc)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
