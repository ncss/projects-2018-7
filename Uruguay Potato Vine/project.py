from microbit import * 
import radio 

#player1

delay = 500

radio.on() 
radio.config(channel = 24) 
block_time = 0
block_disable = 10
block_enable = 4
block_state = True

time = 0

while True: 
    
    x= accelerometer.get_x() 
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    
    if pin0.read_digital() == 1 and block_state == True: 
        print("block" + str(block_time))
        radio.send("Block from player 1") 
        sleep(1000)
        block_time += 1
        if block_time >= block_disable:
            block_state = False
    elif z > 2000 and accelerometer.was_gesture("up"):
        print("fireball" + str(z)) 
        radio.send("Fireball from player 1") 
        sleep(delay) 
    elif x > 2000 and not accelerometer.is_gesture("shake"): 
        print("sideways jab" + str(x))
        radio.send("Sideways jab from player 1") 
        sleep(delay)
    elif button_a.was_pressed():
        print("Insult") 
        radio.send("Insult from player 1")
        sleep(delay)
    elif y > 2000: 
        print("forward punch " + str(y)) 
        radio.send("Forward punch from player 1") 
        sleep(delay)    
        
    if pin0.read_digital() == 0:
        if running_time() >= (time + 1000):
            block_time -= 1
            time = running_time()
        if block_time < 0:
            block_time = 0
        if block_time <= block_enable:
            block_state = True
        
   
    