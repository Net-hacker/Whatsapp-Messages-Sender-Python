import pywhatkit
from pynput.keyboard import Key, Controller
import time
import os

#If you wanna remove the created .txt File let this here else remove that (not recommendet)
if os.path.exists('#Add your path here/pywhatkit_dbs.txt'):
    os.remove('#Add your path here/pywhatkit_dbs.txt' )

#The Script
keyboard = Controller()
print('Have you connected Whatsapp with Whatsapp Web. If not press ctrl + c')
time.sleep(5)
telephone = int(input('Please type the Number (without prefix and spaces): '))
message = str(input('The Message: '))
h = int(input('At what Hour the Message will sented: '))
m = int(input('At what Minute the Message will sented: '))
pywhatkit.sendwhatmsg('#Add your prefix her ' + str(telephone), message, h, m)
keyboard.press(Key.esc)
keyboard.release(Key.esc)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
