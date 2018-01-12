from microbit import *
import protocol as P
import radio

radio.on()
radio.config(channel=P.CHANNEL)

def handle_msg(player, msg):
    if msg == P.DEAD:
        print('player {} has died'.format(player))
    else:
        print('msg {} from player {} ignored'.format(msg, player))

while True:
    msg = radio.receive()

	if msg:
		if msg.startswith(P.PROTOCOL):
            cut = msg.split(':')
            
            # don't trust message
            if len(cut) != 3:
                print('bad msg len {}'.format(msg))
            if not cut[1].isdigit():
                print('ignoring {}, no id'.format(msg))
                
			handle_msg(int(cut[1]), cut[2])
