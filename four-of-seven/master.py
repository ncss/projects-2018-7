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
    if message == "Stop":
        finishTime = running_time() - startTime
        finishingTimes.append(finishTime)
        print(finishingTimes)