These are sample codes for communicating between PC (Windows) and Microbit (or Pyboard).

'serialRead.py' requires "serial" package to be installed on PC.
You need to run serialRead.py file on your PC for waiting signal from Microbit or Pyboard.
When data 'a' is received, the browser (default browser) will be open with the given url.
When data 'b' is received, the browser (chrome.exe) will killed (which means it will close all windows and tabs opened on your chrome)
When data 'c' is received, the browser (default browser) will be open with the given url (In the example, it opens a webpage which will TTS with the specific message).

'serialSend_Sample.py' has three different events you can trigger. 
Press button 1)A, 2)B or 3)both

When button A is pressed, it will send data 'a' 
When button B is pressed, it will send data 'b'
When both buttons are simultaneously pressed, it will send data 'c' 

