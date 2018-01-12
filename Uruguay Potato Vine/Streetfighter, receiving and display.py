from microbit import *
import radio
radio.config(channel = 24)
import random

health_1 = 1000
health_2 = 1000
punch = -20
sideways_jab = -20
fireball = -40


insults= ['Your mother was a hampster and your father smelled of elderberries.', 
'His wit\'s as thick as a Tewkesbury mustard.', 'I am sick when I do look on thee.', 
'Methink\'st thou art a general offence and every man should beat thee.', 
'More of your conversation would infect my brain.', 
'The rankest compound of villainous smell that ever offended nostril.', 
'You are as a candle, the better burnt out.', 
'Thou appeareth nothing to me but a foul and pestilent congregation of vapours.', 
]

radio.on()

while True:
    answer = radio.receive()
    if answer:
        if answer == "Forward punch from player 1":
            print(answer)
            health_2 += punch
            print('Player Two Health: ' + str(health_2))
        if answer == "Sideways jab from player 1":
            print(answer)
            health_2 += sideways_jab
            print('Player Two Health: ' + str(health_2))            
        if answer == "Fireball from player 1":
            print(answer)
            health_2 += fireball
            print('Player Two Health: ' + str(health_2))            
        if answer == "Insult from player 1":
            print(random.choice(insults))
        if answer == "Block from player 1":
            print('Blocked by player 1')
            
        if answer == "Forward punch from player 2":
            print(answer)
            health_2 += punch
            print('Player One Health: ' + str(health_1))
        if answer == "Sideways jab from player 2":
            print(answer)
            health_2 += sideways_jab
            print('Player One Health: ' + str(health_1))            
        if answer == "Fireball from player 2":
            print(answer)
            health_2 += fireball
            print('Player One Health: ' + str(health_1))            
        if answer == "Insult from player 2":
            print(random.choice(insults))
        if answer == "Block from player 2":
            print('Blocked by player 2')
