from microbit import * 
import radio 

#player1

delay = 500

radio.on() 
radio.config(channel = 24) 
block_time = 0
block_disable = 5
block_enable = 4
block_state = True


time = 0

player = 1

while True: 
    
    x= accelerometer.get_x() 
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    disable1 = radio.receive() 
    if disable1: 
        if disable1 == "disable1": 
            sleep(1000) 
            pass  
    else: 
        if pin0.read_digital() == 1 and block_state == True: 
            print("block" + str(block_time))
            radio.send("Block from player " + str(player)) 
            radio.send("disable2") 
            sleep(1000)
            block_time += 1
            if block_time >= block_disable:
                block_state = False
        elif z > 2000 and accelerometer.is_gesture("up"):
            print("fireball " + str(z)) 
            radio.send("Fireball from player " + str(player)) 
            sleep(delay) 
        elif x > 2000 and not accelerometer.is_gesture("shake"): 
            print("sideways jab     " + str(x))
            radio.send("Sideways jab from player " + str(player)) 
            sleep(delay)
        elif button_a.was_pressed():
            print("Insult") 
            radio.send("Insult from player " + str(player))
            sleep(delay)
        elif y > 2000 and accelerometer.is_gesture("face up"): 
            print("forward punch " + str(y)) 
            radio.send("Forward punch from player " + str(player)) 
            sleep(delay)    
            
        if pin0.read_digital() == 0:
            if running_time() >= (time + 1000):
                block_time -= 1
                time = running_time()
            if block_time < 0:
                block_time = 0
            if block_time <= block_enable:
                block_state = True
            
        
        
        
    