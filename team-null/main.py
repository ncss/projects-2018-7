# runs on quokka and relays with relay (i.e. client)
from quokka import *
import protocol as P

# when flashing change this value to the associated device code
# very important
ID = ['1', '2', '3', '4'][0]

radio.enable()
radio.config(channel=P.CHANNEL)

_accellast = (0, 0, 0)

# temporary need derivative
def get_acceldelta():
    global _accellast

    new = (0, 0, )
    
    try:
        new = (accelerometer.x, accelerometer.y, accelerometer.z)
    except Exception as e:
        new = _accellast

        print('accelerometer broke: {}'.format(e))
        
    res = [new[i] - _accellast[i] for i in range(len(new))]
    _accellast = new
    return sum(res)

# test this
_cthresh = 1.0

while True:

    print('waiting for new game to start')

    # wait for (new) game to start
    while True:
        msg = P.get_msg()

        P.send_msg([P.ID, str(ID)])

        if msg and msg[0] == P.START_GAME:
            break

        sleep(P.MSG_RATE)

    print('game started')

    # play game
    while True:
        vel = get_acceldelta()

        if (vel > _cthresh):
            break

    print('waiting for game to end')

    # wait for end game
    while True:
        msg = P.get_msg()
        if msg and msg[0] == P.END_GAME:
            break

        P.send_msg([P.DEAD, ID])
        sleep(P.MSG_RATE)



'''
delta = (accelerometer.x, accelerometer.y, accelerometer.z)

while True:
    newd = (accelerometer.x, accelerometer.y, accelerometer.z)
    #diff = max([abs(a) for a in newd])
    #print ([newd[i] - delta[i] for i in range(len(delta))], diff, diff > 1)

    diff = acc
    
    neopixels.clear()
    for i in range(8):
        if diff > 1: neopixels.set_pixel(i, 50, 0, 0)
        else: neopixels.set_pixel(i, 0, 50, 0)
    neopixels.show()
    newd = delta

    
    
    sleep(100)
    radio.send(PROTOCOL + "hi cameron")
    radio.send(PROTOCOL + ID + ':' + PROTOCOL_DEAD)
'''
