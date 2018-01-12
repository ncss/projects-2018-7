'''
This program is made for the pushuppers controlling the robot
It transmits accelerometer data on channel 34
'''

from microbit import *
import radio

radio.on()
radio.config(channel=34) # sets channel to 34

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    print("x, y, z:", x, y, z)
    sleep(50)
    radio.send(str((x, y, z)))
    if z > 2048:
        radio.send(True)