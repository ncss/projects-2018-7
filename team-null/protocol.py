# i.e. 'joust:4:dead' .. player 4 is dead
from quokka import *

CHANNEL=33
PROTOCOL='joust'
ID='id'
DEAD='dead'
START_GAME='start'
END_GAME='end'

MSG_RATE=int(1000/10)

def get_msg():
    msg = radio.receive()

    if msg:
        msg = msg.split(':')

        if not msg[0] == PROTOCOL:
            return None

        return msg[1:]

    return None

def send_msg(msg_list):
    radio.send(':'.join([PROTOCOL] + msg_list))
