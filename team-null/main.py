# client
from quokka import *

# when flashing change this value to the associated device code
# very important
ID = ['mario', 'luigi', 'yoshi', 'bowser'][0]

# gross
class _p:
    CHANNEL=33
    PROTOCOL='joust'
    ID='id'
    DEAD='dead'
    START_GAME='start'
    END_GAME='end'
    SPEED_UP='sup'
    SLOW_DOWN='sdn'

    THRESH_LOWER=2.0
    THRESH_UPPER=4.0

    MSG_RATE=int(1000/10)

    def __init__(self):
        pass

    def get_msg(self):
        msg = radio.receive()

        if msg:
            msg = msg.split(':')

            if not msg[0] == self.PROTOCOL:
                return None

            return msg[1:]

        return None

    def send_msg(self, msg_list):
        radio.send(':'.join([self.PROTOCOL] + msg_list))

P = _p()

radio.enable()
radio.config(channel=P.CHANNEL)

_Dt = 10
_V = [0, 0, 0]

# integrate accleration
# V = Vo + at
def get_instant_vel():
    global _Dt
    global _V

    # get average V over delta time
    start_time = running_time()
    accel_store = []

    while running_time() < start_time + _Dt or len(accel_store) < 1:
        accel_store.append((accelerometer.x, accelerometer.y, accelerometer.z))

    accel_over_dt = [0, 0, 0]
    accel_over_dt[0] = sum([accel_store[i][0] for i in range(len(accel_store))]) / len(accel_store)
    accel_over_dt[1] = sum([accel_store[i][1] for i in range(len(accel_store))]) / len(accel_store)
    accel_over_dt[2] = sum([accel_store[i][2] for i in range(len(accel_store))]) / len(accel_store)

    #_vinitial = _V

    deriv = [(accel_over_dt[i] * _Dt) - _V[i] for i in range(3)]

    _V[0] = accel_over_dt[0] * _Dt
    _V[1] = accel_over_dt[1] * _Dt
    _V[2] = accel_over_dt[2] * _Dt
    
    #try:
    #    new = (accelerometer.x, accelerometer.y, accelerometer.z)
    #except Exception as e:
    #    new = _accellast
    #    print('accelerometer broke: {}'.format(e))
        
    ret = ((deriv[0] * deriv[0]) + (deriv[1] * deriv[1]) + (deriv[2] * deriv[2])) ** (1/2)

    print(_V, ret, ret - 9.8)

    #_vinitial = _V

    return ret

# test this
_cthresh = P.THRESH_UPPER

while True:
    v = get_instant_vel()

    if v > 1.5:
        for i in range(8):
            neopixels.set_pixel(i, 64, 0, 0)
    else:
        for i in range(8):
            neopixels.set_pixel(i, 0, 64, 0)

    neopixels.show()
    
    sleep(100)

exit(1)

while True:

    print('waiting for new game to start')
    print('my id is: {}'.format(ID))

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

        msg = P.get_msg()
        if msg:
            if msg[0] == P.END_GAME:
                break
            
            if msg[0] == P.SPEED_UP:
                _cthresh = P.THRESH_UPPER
                print('speeding up...')
                
            if msg[0] == P.SLOW_DOWN:
                _cthresh = P.THRESH_LOWER

                print('slowing down...')

    print('waiting for game to end')

    # wait for end game
    while True:
        msg = P.get_msg()
        if msg and msg[0] == P.END_GAME:
            break

        P.send_msg([P.DEAD, ID])
        sleep(P.MSG_RATE)
