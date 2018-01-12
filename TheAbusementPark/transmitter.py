from microbit import * 
import radio

CHANNEL = 22
PROTOCOL = "hex:"

radio.config(channel=CHANNEL)
radio.on()

while True:
    display.show(Image.TARGET)
    if button_a.was_pressed():
        radio.send(PROTOCOL + "left")
    elif button_b.was_pressed():
        radio.send(PROTOCOL + "right")




