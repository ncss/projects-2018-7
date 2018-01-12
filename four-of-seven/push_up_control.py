"""
This program is made for the pushuppers controlling the robot
It transmits accelerometer data on channel 34
"""


from microbit import *
import radio


CHANNEL = 34
PUSH_UP_ACCELERATION_THRESHOLD = 1200
MOTORS = ['L', 'R']
ROBOTS = ['A']


radio.on()
radio.config(channel=CHANNEL) # sets channel to 34


was_over_threshold = abs(accelerometer.get_z()) >= \
    PUSH_UP_ACCELERATION_THRESHOLD
motor_index = 0
robot_index = 0
get_robot_id = lambda: ROBOTS[robot_index % len(ROBOTS)]
get_motor_id = lambda: MOTORS[motor_index % len(MOTORS)]


while True:
    if button_a.was_pressed():
        robot_index += 1
    if button_b.was_pressed():
        motor_index += 1
    
    display.show([get_robot_id(), get_motor_id()])

    z_axis_acceleration = accelerometer.get_z()
    print(z_axis_acceleration)
    if abs(z_axis_acceleration) >= PUSH_UP_ACCELERATION_THRESHOLD and not \
            was_over_threshold:
        was_over_threshold = True
        radio.send(get_motor_id())
        print('Transmitted {}.'.format(get_motor_id()))
    elif abs(z_axis_acceleration) < PUSH_UP_ACCELERATION_THRESHOLD:
        was_over_threshold = False
