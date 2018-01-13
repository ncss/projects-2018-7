# client
from quokka import *
import math

# when flashing change this value to the associated device code
# very important
ID = ['mario', 'yoshi', 'peach', 'bowser'][2]

ID_COLORS = {
    'mario' : (255, 0, 0),
    'yoshi' : (0, 255, 0),
    'peach' : (255, 10, 50),
    'bowser' : (255, 200, 0)
}

ANIM_TIME = 2000

PI_3 = (math.pi * 2.0 ) / 3.0

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

    THRESH_LOWER=8.0
    THRESH_UPPER=10.0

    MSG_RATE=int(1000/10)

    def __init__(self):
        pass

    def get_msg(self):
        try:
            msg = radio.receive()

            if msg:
                msg = msg.split(':')

                if not msg[0] == self.PROTOCOL:
                    return None

                return msg[1:]

            return None
        except:
            return None

    def send_msg(self, msg_list):
        radio.send(':'.join([self.PROTOCOL] + msg_list))

P = _p()

radio.enable()
radio.config(channel=P.CHANNEL)

_Dt = 10

def get_accel():
    global _Dt

    # get average V over delta time
    start_time = running_time()
    accel_store = []

    while running_time() < start_time + _Dt or len(accel_store) < 1:
        try:
            accel_store.append((accelerometer.x, accelerometer.y, accelerometer.z))
        except Exception as e:
            print('accelerometer broke: {}'.format(e))

    accel_over_dt = [0, 0, 0]
    accel_over_dt[0] = (sum([accel_store[i][0] for i in range(len(accel_store))]) / len(accel_store)) * _Dt
    accel_over_dt[1] = (sum([accel_store[i][1] for i in range(len(accel_store))]) / len(accel_store)) * _Dt
    accel_over_dt[2] = (sum([accel_store[i][2] for i in range(len(accel_store))]) / len(accel_store)) * _Dt

    return (((accel_over_dt[0] ** 2) + (accel_over_dt[1] ** 2) + (accel_over_dt[2] ** 2)) ** (1/2)) - (9.8)

def set_lights(col):
    for i in range(8):
        neopixels.set_pixel(i, col[0], col[1], col[2])
        
    neopixels.show()

# test this
_cthresh = P.THRESH_UPPER

while True:
    
    am_dead = False

    print('waiting for new game to start')
    print('my id is: {}'.format(ID))

    # wait for (new) game to start
    while True:
        set_lights((0, 0, 0) if ((running_time() // 1000) % 2) else ID_COLORS[ID])
        
        msg = P.get_msg()

        P.send_msg([P.ID, str(ID)])

        if msg and msg[0] == P.START_GAME:
            break

        sleep(P.MSG_RATE)

    print('game started')

    # play game
    while True:
        set_lights(ID_COLORS[ID])
        
        vel = get_accel()
        
        if (abs(vel) > _cthresh):
            am_dead = True
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

    set_lights((0, 0, 0))

    # wait for end game
    while True:
        msg = P.get_msg()
        if msg and msg[0] == P.END_GAME:
            if am_dead:
                set_lights((0, 0, 0)) # loser
                sleep(ANIM_TIME)
            else:
                st = running_time()
                
                # winner
                while running_time() < st + ANIM_TIME:
                    Q = running_time() / 10

                    for i in range(8):
                        neopixels.set_pixel_rainbow(i, int((3*i+Q)%119))
                    neopixels.show()
                    
            break

        P.send_msg([P.DEAD, ID])
        sleep(P.MSG_RATE)
