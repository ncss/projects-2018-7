from microbit import *
import radio

radio.on()
radio.config(channel=34)

startTime = 0

# M is for master.
display.show('M')

while True:
    message = radio.receive()
    if button_a.was_pressed():
        radio.send("Start")
        startTime = running_time()
        display.scroll('ON', wait=False, loop=True)
    if message == "Stop":
        finish_time = running_time() - startTime
        display.scroll('OFF', wait=False, loop=True)
        print(finish_time)
