import webbrowser
import serial
import time
import os
from time import sleep

#How to find USB Serial Port? - Go to "Device Manager" and see under Ports (COM & LPT)
ser = serial.Serial('COM5', 115200, timeout=0)
#ser.open()
while True:
	data = ser.readline().strip()
	if len(data) > 0:
		print (data)
		#when data "a" stays in received data open webbrowser with the given link 
		if("'a'" in str(data)):
			webbrowser.open("https://youtu.be/WApIDsZaNfI")
		#when data "b" stays in received data kill chrome.exe (This will kill all windows and tabs)
		elif("'b'" in str(data)):
			browserExe = "chrome.exe"    
			os.system("taskkill /f /im "+browserExe)
		#when data "c" stays in received data open webbrowser with the given link  (sample for TTS)
		if("'c'" in str(data)):
			msg = "Hello there, this is testing."
			webbrowser.open("http://ncss.davidchungproject.com/?msg=" + msg)
	sleep(0.5)
			
ser.close()

