#!/usr/bin/python
#python 3.7.3
#Useage
#/path/to/script <what to search for>
#<what to search for> can be, but is not limited to, song name or artist name or both


import os
import webbrowser
import pyautogui
import pyscreenshot as ImageGrab
from time import sleep
import sys
from PIL import Image

if len(sys.argv) > 1: #this means execute code only if search parameter is provided
	URL = 'https://musicpleer.media/'

	webbrowser.open(URL)

	sleep(15) #give time to load webpage

	pyautogui.press('f11') # enter full screen mode

	pyautogui.moveTo(217,157, duration = 0.5) #co-ordinates of recent search dropdown
	pyautogui.click()#close recent searches drop down

	pyautogui.moveTo(244,105, duration = 0.2) #search bar co-ordinates
	pyautogui.click() #select search bar

	search_term = ' '.join(sys.argv[1:])

	pyautogui.write(search_term, interval = 0.1)#write search term
	sleep(5)# pause for a moment
	pyautogui.press('enter') #submit query
	sleep(2.2)

	im = ImageGrab.grab() #take screenshot

	if not os.path.isdir('./check'): #if check directory does not exists in current working directory
		os.makedirs('./check') #then create it

	im.save('./check/screen.png') #save in check folder in current directory as 'screen.png'

	#check if error occured
	image = Image.open('./check/screen.png')# open image
	pix = image.load()
	value = pix[603,410]# RBG value of this pixel

	if value == (197, 70, 70): #if RBG value pixel at (603, 410) matches, then error occured
		raise Exception('Not Found')

	pyautogui.moveTo(527,178, duration = 0.5) #move cursor to first result
	pyautogui.click() #select song

	pyautogui.moveTo(517,264, duration = 0.5) #move cursor to download button
	pyautogui.rightClick()
	pyautogui.press('k') #keyboard shortcut for 'save-link'

	sleep(3) #time for save dialog box to open

	pyautogui.press('enter') #download starts in folder
	print("Download Started...")
else:
	raise Exception('No search parameter provided\n'
					'#Useage\n'
					'#/path/to/script <what to search for>\n'
					'#<what to search for> can be, but is not limited to, song name or artist name or both')