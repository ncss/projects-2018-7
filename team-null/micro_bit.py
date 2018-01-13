# server
from microbit import *
import radio

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

radio.on()
radio.config(channel=P.CHANNEL)

registered_ids = []

while True:
    print('waiting for users to join')    
    
    # temp should wait for timer
    while len(registered_ids) < 3:
        if button_a.was_pressed():
            print('playing with only {} people'.format(len(registered_ids)))
            break
            
        msg = P.get_msg()
        #print(msg, registered_ids)
        if msg and msg[0] == P.ID:
            if msg[1] not in registered_ids:
                registered_ids.append(msg[1])

                print('registered player {}'.format(msg[1]))

    print('starting game')

    # TODO: implement quokka received check
    for i in range(5):
        P.send_msg([P.START_GAME])
        sleep(P.MSG_RATE)

    while len(registered_ids) > 1:

        # TODO: implement quokka received check
        if button_a.was_pressed():
            for i in range(5):
                P.send_msg([P.SPEED_UP])
                sleep(P.MSG_RATE)
                
        if button_b.was_pressed():
            for i in range(5):
                P.send_msg([P.SLOW_DOWN])
                sleep(P.MSG_RATE)
        
        msg = P.get_msg()

        if msg:
            if msg[0] == P.DEAD and msg[1] in registered_ids:
                registered_ids.remove(msg[1])

                print('player {} has died, {} remain'.format(msg[1], len(registered_ids)))

    if len(registered_ids) == 1:
        print('game over, player {} has won'.format(registered_ids[0]))
    else:
        print('something went very wrong')

    # TODO: implement quokka received check
    for i in range(5):
        P.send_msg([P.END_GAME])
        sleep(P.MSG_RATE)
