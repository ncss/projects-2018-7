from microbit import *
import radio

CHANNEL = 22
PROTOCOL = "hex:"
DELAY_CYCLE = 2000

radio.config(channel=CHANNEL)
radio.on()

while True:
    msg = radio.receive()
    if msg and msg.startswith(PROTOCOL):
        if msg == PROTOCOL + "left":
            display.clear()
            display.show(Image.ARROW_W, delay=DELAY_CYCLE, wait=False, clear=True)
        elif msg == PROTOCOL + "right":
            display.clear()
            display.show(Image.ARROW_E, delay=DELAY_CYCLE, wait=False, clear=True)
        elif msg == PROTOCOL + "up":
            display.clear()
            display.show(Image.ARROW_N, delay=DELAY_CYCLE, wait=False, clear=True)
        elif msg == PROTOCOL + "down":
            display.clear()
            display.show(Image.ARROW_S, delay=DELAY_CYCLE, wait=False, clear=True)
