from microbit import * 
import radio 

health = 1000 
pdamage = 20 
fdamage = 40 

while True: 
    
    x= accelerometer.get_x() 
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    if y > 2000: 
        print("forward punch " + str(y)) 
        sleep(500)
        health = health - pdamage 
    '''if y > 2000 and pin0.read_digital() == 1: 
        print("fireball" + str(z)) 
        sleep(500) 
        health = health - fdamage  '''
        
    