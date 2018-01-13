from microbit import *

def across_line():
    
    light_1 = pin1.read_analog()
    light_2 = pin2.read_analog()
    
    print ("light_1:" + str(light_1))
    print ("light_2:" + str(light_2))
    
    if light_1 < 10 and light_2 <10:
        return True
    
    return False
    
while True:
    if across_line():
        print("STOP")
        sleep(2000)
        
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

    
    