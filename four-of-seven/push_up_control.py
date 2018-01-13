"""
This program is made for the pushuppers controlling the robot. It transmits
accelerometer data on channel 34.
"""


from microbit import *
import radio
import music


CHANNEL = 34
# Detects upward part of pushup.
PUSH_UP_ACCELERATION_THRESHOLD = -1100
MOTORS = ['L', 'R']


radio.on()
radio.config(channel=CHANNEL) # sets channel to 34


was_over_threshold = False
motor_index = 0


while True:
    if button_b.was_pressed():
        motor_index = not motor_index

    display.show(MOTORS[motor_index])

    z_axis_acceleration = accelerometer.get_z()
    # Smaller than because upwards acceleration is negative.
    if z_axis_acceleration <= PUSH_UP_ACCELERATION_THRESHOLD and not \
            was_over_threshold:
        was_over_threshold = True
        music.play(music.BA_DING)
        radio.send(MOTORS[motor_index])
        print(
            'Transmitted {}, after acceleration of {}.'.format(
                MOTORS[motor_index],
                z_axis_acceleration
            )
        )
    elif z_axis_acceleration > PUSH_UP_ACCELERATION_THRESHOLD:
        was_over_threshold = False
