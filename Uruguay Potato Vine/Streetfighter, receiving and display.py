from microbit import *
import radio
radio.config(channel = 24)
import random
import music

health_1 = 1000
health_2 = 1000
punch = -20
sideways_jab = -30
fireball = -40


insults= ['Your mother was a hampster and your father smelled of elderberries.', 
'His wit\'s as thick as a Tewkesbury mustard.', 'I am sick when I do look on thee.', 
'Methink\'st thou art a general offence and every man should beat thee.', 
'More of your conversation would infect my brain.', 
'The rankest compound of villainous smell that ever offended nostril.', 
'You are as a candle, the better burnt out.', 
'Thou appeareth nothing to me but a foul and pestilent congregation of vapours.', 
]

while True:
    if button_a.was_pressed():
        music.play(music.ENTERTAINER)
        radio.on()
    if button_b.was_pressed():
        music.play(music.NYAN)
        radio.off()

while True:
    answer = radio.receive()
    if answer:
        if answer:
            music.stop()
        if answer == "Forward punch from player 1" and not "Blocked by player 2":
            print(answer)
            health_2 += punch
            print('Player Two Health: ' + str(health_2)+ '\n')
        if answer == "Sideways jab from player 1":
            print(answer)
            health_2 += sideways_jab
            print('Player Two Health: ' + str(health_2)+ '\n')            
        if answer == "Fireball from player 1":
            print(answer)
            health_2 += fireball
            print('Player Two Health: ' + str(health_2) + '\n')
        if answer == "Insult from player 1":
            choice = random.choice(insults)
            print(choice + '\n')
            if choice == insults[0]:
                music.play(music.PYTHON, wait=False)
        if answer == "Block from player 1":
            print('Blocked by player 1' + '\n')
            
        if answer == "Forward punch from player 2":
            print(answer)
            health_1 += punch
            print('Player One Health: ' + str(health_1)+ '\n')
        if answer == "Sideways jab from player 2":
            print(answer)
            health_1 += sideways_jab
            print('Player One Health: ' + str(health_1)+ '\n')            
        if answer == "Fireball from player 2":
            print(answer)
            health_1 += fireball
            print('Player One Health: ' + str(health_1)+ '\n')            
        if answer == "Insult from player 2":
            choice = random.choice(insults)
            print(choice + '\n')
            if choice == insults[0]:
                music.play(music.PYTHON, wait=False)
        if answer == "Block from player 2":
            print('Blocked by player 2' + '\n')
#player 1
if health_2 == 0:
    display.show(Image.HAPPY)
    music.play(music.POWER_UP)
if health_1 == 0:
    display.show(Image.SAD)
    music.play(music.WAWAWAWAA)

#player 2
if health_1 == 0:
    display.show(Image.HAPPY)
    music.play(music.POWER_UP)
if helath_2 ==0:
    display.show(Image.SAD)
    music.play(music.WAWAWAWAA)