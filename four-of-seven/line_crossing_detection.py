from microbit import *

def across_line():
    return False
    
while True:
    if across_line():
        break
        
    pin0.write_digital(1)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(1)
    sleep(5)
    pin0.write_digital(0)
    pin16.write_digital(0)
    pin12.write_digital(0)
    pin8.write_digital(0)    
    sleep(15)

    
    