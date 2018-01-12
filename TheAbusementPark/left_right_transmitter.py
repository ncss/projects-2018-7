from microbit import * 
import radio

CHANNEL = 22
PROTOCOL = "hex:"
LEFT_RIGHT_ART = Image("00000:09090:99999:09090:00000")

radio.config(channel=CHANNEL)
radio.on()

while True:
    display.show(LEFT_RIGHT_ART)
    if pin0.read_digital():
        radio.send(PROTOCOL + "left")
    elif pin1.read_digital():
        radio.send(PROTOCOL + "right")
    sleep(50)


