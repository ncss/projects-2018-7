from microbit import *
import radio
import music

CHANNEL = 22
PROTOCOL = "hex:"
DELAY_CYCLE = 2000

radio.config(channel=CHANNEL)
radio.on()

# avoid spam from users as there is no current fix for it right now

while True:
    msg = radio.receive()
    if msg:
        if not msg.startswith(PROTOCOL):
            print(msg)
            continue
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
        elif msg == PROTOCOL + "game_over":
            display.clear()
            display.show(Image.SAD, delay=DELAY_CYCLE, loop=False, clear=True)
            music.play(music.GREENSLEEVES, wait=False)
            display.scroll("Game Over!!!", loop=True)
   sleep(50)
