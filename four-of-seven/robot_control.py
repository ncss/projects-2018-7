from microbit import *
import radio


# Motor data:


MOTOR_RUN_TIME = 300
pushupCounter = 0
lEndTime = 0
rEndTime = 0
startFlag = False


# Colour detection data


# If any sensor is seeing brighted (lower) than this, it can be considered on.
THRESHOLD = 590
# If red and green are on, that is white, if they are both off, that is red.
RED_PIN = pin1
GREEN_PIN = pin2

detected_colour = lambda pin: pin.read_analog() < THRESHOLD
on_red = lambda: detected_colour(RED_PIN) and not detected_colour(GREEN_PIN)
on_green = lambda: detected_colour(GREEN_PIN) and not detected_colour(RED_PIN)
on_white = lambda: detected_colour(GREEN_PIN) and detected_colour(RED_PIN)


order = [on_red, on_green, on_white]
position_in_order = 0


radio.on()
radio.config(channel=34) # sets channel to 34


# motors 0 8 12 16, 12 (right forward) 16 (left forward)
def driveLeftMotor():
    pin0.write_digital(0)
    pin16.write_digital(1)


def driveRightMotor():
    pin12.write_digital(1)


def stopLeft():
    pin0.write_digital(0)
    pin16.write_digital(0)


def stopRight():
    pin12.write_digital(0)


while True:
    # Handle colour detection:

    print('Step: {}.'.format(position_in_order))
    try:
        if order[position_in_order]():
            position_in_order += 1
    except:
        print("Finished")
        startFlag = False
        radio.send("Stop")

    if button_a.was_pressed():
        position_in_order = 0

    message = radio.receive()
    if running_time() > lEndTime:
        stopLeft()
    if running_time() > rEndTime:
        stopRight()

    # Signal sent to robot from master to start.
    if message == "Start":
        startFlag = True

    # Message received and instructed to start.
    if message and startFlag == True:
        # If a message is received (if threshold is met).
        pushupCounter += 1
        print(pushupCounter)

        # Drive left motor.
        if message == "L":
            print("getting L")
            lEndTime = running_time() + MOTOR_RUN_TIME
            driveLeftMotor()

        # Drive right motor.
        elif message == "R":
            print("getting R")
            rEndTime = running_time() + MOTOR_RUN_TIME
            driveRightMotor()
