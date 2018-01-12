from microbit import * 
import radio

CHANNEL = 22
PROTOCOL = "hex:"

radio.config(channel=CHANNEL)
radio.on()

while True:
    display.show(Image.TARGET)
    if pin0.read_digital():
        radio.send(PROTOCOL + "left")
    elif pin1.read_digital():
        radio.send(PROTOCOL + "right")
    elif pin2.read_digital():
        radio.send(PROTOCOL + "up")



