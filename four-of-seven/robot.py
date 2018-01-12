from microbit import *
import radio

radio.on()
radio.config(channel=34) # sets channel to 34

def driveFwd():
    pin0.write_digital(0)
    pin16.write_digital(1)
    pin12.write_digital(1)
    pin8.write_digital(0)
    
while True:
    message = radio.receive()
    print(message)
    if message == True:
        driveFwd()
        sleep(500)