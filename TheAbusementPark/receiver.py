from microbit import *
import radio

CHANNEL = 22
PROTOCOL = "hex:"

radio.config(channel=CHANNEL)
radio.on()

while True:
    msg = radio.receive()
    if msg and msg.startswith(PROTOCOL):
        if msg == PROTOCOL + "left":
            display.clear()
            display.show(Image.ARROW_W, delay=2000, wait=False, clear=True)
        elif msg == PROTOCOL + "right":
            display.clear()
            display.show(Image.ARROW_E, delay=2000, wait=False, clear=True)
        
        
