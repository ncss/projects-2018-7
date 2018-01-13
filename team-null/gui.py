import pygame
import webbrowser
import serial
import time
import os
from time import sleep

C_WIDTH=1280
C_HEIGHT=720
C_FLAGS=pygame.FULLSCREEN

COM_NUM = 13
BLACK = (0,0,0)
TEXT = (255, 255, 255)
WAITING = 0
IN_GAME = 1
GAME_OVER = 2
BG = {
    WAITING : (255, 0, 0),
    IN_GAME : (0, 255, 0),
    GAME_OVER: (0, 0, 255)
}

ser = serial.Serial('COM' + str(COM_NUM), 115200, timeout=0)

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
        msg_set = ':'.join([self.PROTOCOL] + msg_list)
        radio.send(msg_set)
        
    def send_serial(self, msg_list):
        msg_set = ':'.join([self.PROTOCOL] + msg_list)
        print(msg_set)

P = _p()

def read_from_serial(ser):
    sleep(0.05)
    
    data = ser.readline().strip()
    if data:
        data = data.decode('utf-8')
        print (data)
        data = data.split(":")
        if not data[0] == P.PROTOCOL:
            print("ran")
            return None

        return data[1:]
    return None
        
class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.size = (C_WIDTH, C_HEIGHT)
        self.screen = pygame.display.set_mode(self.size, C_FLAGS)
        self.should_quit = False
        self.screen_phase = WAITING
        self.current_players = []

    def loop(self):
        data = read_from_serial(ser)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_quit = True
            #if event.type == 

        # temp
        font = pygame.font.SysFont("ubuntu", 70)
        bigfont = pygame.font.SysFont("ubuntu", 100)
        self.screen.fill(BG[self.screen_phase])
        #pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        if self.screen_phase == WAITING:
            heading = font.render("Waiting for players to join", True, TEXT)
            self.screen.blit(heading, (((C_WIDTH - heading.get_rect().width)/2), 50))
            for i in range(len(self.current_players)):
                player = font.render(self.current_players[i], True, TEXT)
                self.screen.blit(player, (((C_WIDTH - player.get_rect().width)/2), 100*(i+2)))
            if data:
                print(data)
            if data and len(data) > 0:
                if data[0] == P.ID and data[1] not in self.current_players and len(data) > 1:
                    self.current_players.append(data[1])
                if data[0] == P.START_GAME:
                    self.screen_phase = IN_GAME
                    #nfont = pygame.font.SysFont("monospace", 70)
                    #player = nfont.render(data[1], True, BLACK)
                    #print(data[1])
                    #self.screen.blit(player, (((C_WIDTH - heading.get_rect().width)/2), 100*(len(self.current_players)+1)))

        elif self.screen_phase == IN_GAME:
            heading = bigfont.render("Active Players", True, TEXT)
            self.screen.blit(heading, (((C_WIDTH - heading.get_rect().width)/2), 50))
            for i in range(len(self.current_players)):
                player = font.render(self.current_players[i], True, TEXT)
                self.screen.blit(player, (((C_WIDTH - player.get_rect().width)/2), 100*(i+2)))
            if data and len(data) > 1:
                if data[0] == P.DEAD:
                    if data[1] in self.current_players:
                        self.current_players.remove(data[1])
            if len(self.current_players) == 1:
                self.screen_phase = GAME_OVER
                # sleep(2)
        elif self.screen_phase == GAME_OVER:
            heading = bigfont.render(self.current_players[0].upper() + " WINS!!!!", True, TEXT)
            self.screen.blit(heading, (((C_WIDTH - heading.get_rect().width)/2), ((C_HEIGHT - heading.get_rect().height)/2)))
            sleep(2)
            if data and len(data) == 1 and data[0] == P.END_GAME:
                self.screen_phase = WAITING
                
        else:
            heading = font.render("SOMETHING WENT WRONG!!!", True, TEXT)
            self.screen.blit(heading, (((C_WIDTH - heading.get_rect().width)/2), ((C_HEIGHT - heading.get_rect().height)/2)))
        pygame.display.flip()
        
    def close(self):
        pygame.quit()

    def closing(self):
        return self.should_quit

g = Game()

try:
    while not g.closing():
        g.loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.should_quit = True
    g.close()
except SystemExit:
    g.close()
