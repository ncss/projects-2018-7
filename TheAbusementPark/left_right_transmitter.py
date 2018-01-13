from microbit import * 
import radio

CHANNEL = 22
PROTOCOL = "hex:"
LEFT_RIGHT_ART = Image("00000:09090:99999:09090:00000")
BTN_DELAY = 100
PRESS_TIME = 0
PIN0 = 0
PIN1 = 1

btn_states = [False, False]
radio.config(channel=CHANNEL)
radio.on()

while True:
    now = running_time()
    # display.show(LEFT_RIGHT_ART)
    if True in btn_states:
        if pin0.read_digital():
            btn_states[PIN0] = True    
        if pin1.read_digital():
            btn_states[PIN1] = True
    else:
        btn_states = pin0.read_digital()
        btn_states = pin1.read_digital()
        
        PRESS_TIME = now

    time_diff = PRESS_TIME - now
    print(time_diff)

    sleep(50)


