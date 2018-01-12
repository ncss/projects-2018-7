from microbit import * 
import radio

CHANNEL = 22
PROTOCOL = "hex:"
UP_DOWN_ART = Image("00900:09990:00900:09990:00900")

radio.config(channel=CHANNEL)
radio.on()

while True:
    display.show(UP_DOWN_ART)
    if pin0.read_digital():
        radio.send(PROTOCOL + "up")
    elif pin1.read_digital():
        radio.send(PROTOCOL + "down")
    sleep(50)


