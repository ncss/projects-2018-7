from microbit import *
import radio
radio.config(channel = 24)
import random
import music
radio.on()

health_1 = 1000
health_2 = 1000
punch = -20
sideways_jab = -30
fireball = -40

display.show(Image.HAPPY)


insults= ['Your mother was a hampster and your father smelled of elderberries.', 
'His wit\'s as thick as a Tewkesbury mustard.', 'I am sick when I do look on thee.', 
'Methink\'st thou art a general offence and every man should beat thee.', 
'More of your conversation would infect my brain.', 
'The rankest compound of villainous smell that ever offended nostril.', 
'You are as a candle, the better burnt out.', 
'Thou appeareth nothing to me but a foul and pestilent congregation of vapours.', 
]
gameon = True 
while gameon == True:
    '''if button_a.was_pressed():
        music.play(music.ENTERTAINER)
        radio.on()
    if radio.on:
        if button_b.was_pressed():
            music.play(music.NYAN)
            radio.off()'''

    answer = radio.receive()
    if answer:
        music.stop()
    if answer == "Block from player 1" or answer == "Block from player 2":
        print('Blocked' + '\n')
        #sleep(1000)
    else: 
        if answer == "Forward punch from player 1":
            print(answer)
            health_2 += punch
            print('Player Two Health: ' + str(health_2)+ '\n')
            radio.send('player2_health:{}'.format(health_2))
        if answer == "Sideways jab from player 1":
            print(answer)
            health_2 += sideways_jab
            print('Player Two Health: ' + str(health_2)+ '\n')
            radio.send('player2_health:{}'.format(health_2))
        if answer == "Fireball from player 1":
            print(answer)
            health_2 += fireball
            print('Player Two Health: ' + str(health_2) + '\n')
            radio.send('player2_health:{}'.format(health_2))
        if answer == "Insult from player 1":
            choice = random.choice(insults) 
            radio.send("Player 1 says: " + choice) 
            ttsChoice = random.randrange(0,7)
            radio.send("TTS:" + str(ttsChoice)) 
            
            print("Player 1 says: " + choice + '\n')
            if choice == insults[0]:
                music.play(music.PYTHON, wait=False)

            
        if answer == "Forward punch from player 2":
            print(answer)
            health_1 += punch
            print('Player One Health: ' + str(health_1)+ '\n')
            radio.send('player1_health:{}'.format(health_1))
        if answer == "Sideways jab from player 2":
            print(answer)
            health_1 += sideways_jab
            print('Player One Health: ' + str(health_1)+ '\n')  
            radio.send('player1_health:{}'.format(health_1))
        if answer == "Fireball from player 2":
            print(answer)
            health_1 += fireball
            print('Player One Health: ' + str(health_1)+ '\n')
            radio.send('player1_health:{}'.format(health_1))
        if answer == "Insult from player 2":
            choice = random.choice(insults)
            radio.send("Player 2 says: " + choice) 
            ttsChoice = random.randrange(0,7)
            radio.send("TTS:" + str(ttsChoice))
            print("Player 2 says: " + choice + '\n')
            if choice == insults[0]:
                music.play(music.PYTHON, wait=False)
        
        loop = 0    
        #player 1
        if health_2 <= 0:
            while loop < 10:  
                radio.send("player1_win")
                loop+=1
                sleep(100)
            gameon = False 
        if health_1 <= 0:
            while loop < 10:
                radio.send("player2_win")
                loop+=1
                sleep(100)
            gameon = False 
            
display.show(Image.SAD)
