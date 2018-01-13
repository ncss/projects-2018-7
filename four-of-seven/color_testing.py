from microbit import *

pin1List = []
pin2List = []

testNow = False

print("Press A button to start testing. Pressing A button will stop testing.")
print("Press B button to reset result")

while True:
    if(button_a.was_pressed()):
        testNow = not testNow
        print("Testing stopped. Press A button to re-start testing")
        
    if(button_b.was_pressed()):
        pin1List = []
        pin2List = []
        print("Resetting testing result.")
        
    if testNow:
        pin1Read = pin1.read_analog() 
        pin2Read = pin2.read_analog() 
        
        if pin1Read not in pin1List:
            pin1List.append(pin1Read)
        
        if pin2Read not in pin2List:
            pin2List.append(pin2Read)
        
        print("pin1: ") 
        print(sorted(pin1List))
        print("pin2: ")
        print(sorted(pin2List))
        
        sleep(500)
        
    
    
