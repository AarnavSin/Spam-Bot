'''
Enjoy! Very basic script that allows you to spam text. 
Use this to annoy someone.
'''

import pyautogui, time
#Imports necessary modules.

f = open("insert plain text file directory here", 'r')
#Opens text file.

time.sleep(5)
#Time before it starts typing.

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
#Main script. 