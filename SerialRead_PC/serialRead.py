import webbrowser
import serial
import time
import os
from time import sleep

#How to find USB Serial Port? - Go to "Device Manager" and see under 
ser = serial.Serial('COM5', 115200, timeout=0)
#ser.open()
while True:
    data = ser.readline()
    if len(data) > 0:
		#when data "a" stays in received data open webbrowser with the given link 
        if("a" in str(data)):
            webbrowser.open("https://youtu.be/WApIDsZaNfI")
		#when data "b" stays in received data kill chrome.exe (This will kill all windows and tabs)
        elif("b" in str(data)):            
            browserExe = "chrome.exe"    
            os.system("taskkill /f /im "+browserExe)
    sleep(0.5)
			
ser.close()

