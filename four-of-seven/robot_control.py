from microbit import *
import radio

# motors 0 8 12 16, 12 (right forward) 16 (left forward)

radio.on()
radio.config(channel=34) # sets channel to 34

THRESHOLD = 0
MOTOR_RUN_TIME = 300
pushupCounter = 0
lEndTime = 0
rEndTime = 0

def driveFwd():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_digital(1)
    pin8.write_digital(0)

def driveLeftMotor():
    pin0.write_digital(0)
    pin16.write_digital(1)

def driveRightMotor():
    pin12.write_digital(1)

def driveBwd():
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(1)
    
def stop():
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(0)
    
def stopLeft():
    pin0.write_digital(0)
    pin16.write_digital(0)
    
def stopRight():
    pin12.write_digital(0)

"""def driveLeft():
    pin0.write_analog(0)
    pin16.write_analog(512)
    pin12.write_analog(1023)
    pin8.write_analog(0)

def driveRight():
    pin0.write_analog(0)
    pin16.write_analog(1023)
    pin12.write_analog(512)
    pin8.write_analog(0)"""
    
while True:
    message = radio.receive()
    if running_time() > lEndTime:
        stopLeft()
    if running_time() > rEndTime:
        stopRight()    
    if message: # if a message is received (if threshold is met)
    
        pushupCounter += 1
        print(pushupCounter)
    
        # drive left motor
        if message == "L":
            print("getting L")
            lEndTime = running_time() + MOTOR_RUN_TIME
            driveLeftMotor()
                
                
        # drive right motor
        elif message == "R":
            print("getting R")
            rEndTime = running_time() + MOTOR_RUN_TIME
            driveRightMotor()