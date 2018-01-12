from microbit import *
import radio

CHANNEL = 22
PROTOCOL = 'hex:'
radio.on()
radio.config(channel=CHANNEL)

#box
while True:
    message = PROTOCOL + "game_over"
    measurement_x = accelerometer.get_x()
    measurement_y = accelerometer.get_y()
    measurement_z = accelerometer.get_z()
    sleep(10)
    condition_x = measurement_x - accelerometer.get_x()
    condition_y = measurement_y - accelerometer.get_y()
    condition_z = measuremeny_x - accelerometer.get_z()
    if condition_x > 300 or condition_x < -300:
        radio.send(message)
    if condition_y > 300 or condition_y < -300:
        radio.send(message)
    if condition_z > 300 or condition_z < -300:
        radio.send(message)

#pipe
while True:
    if accelerometer.current_gesture() != 'facedown':
        radio.send(message)
        print('hi')