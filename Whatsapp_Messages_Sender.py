import pywhatkit
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
print('Have you connected Whatsapp with Whatsapp Web. If not press ctrl + c')
time.sleep(5)
telephone = int(input('Please type the Number (without prefix and spaces): '))
message = str(input('The Message: '))
h = int(input('At what Hour the Message will sented: '))
m = int(input('At what Minute the Message will sented: '))
pywhatkit.sendwhatmsg('+49 ' + str(telephone), message, h, m)
keyboard.press(Key.esc)
keyboard.release(Key.esc)
keyboard.press(Key.enter)
keyboard.release(Key.enter)