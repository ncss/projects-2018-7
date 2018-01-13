from microbit import *
import radio

radio.on()
radio.config(channel=34)

startTime = 0
finishingTimes = []

# M is for master.
display.show('M')

while True:
    message = radio.receive()
    if button_a.was_pressed():
        radio.send("Start")
        startTime = running_time()
        display.scroll('ON', wait=False, loop=True)
    if message == "Stop":
        finishTime = running_time() - startTime
        finishingTimes.append(finishTime)
        display.scroll('OFF', wait=False, loop=True)
        print(finishingTimes)