import pygame

C_WIDTH=1280
C_HEIGHT=720
C_FLAGS=0

class Game:
    def __init__(self):
        pygame.init()
        self.size = (C_WIDTH, C_HEIGHT)
        self.screen = pygame.display.set_mode(self.size, C_FLAGS)
        self.should_quit = False

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.should_quit = True
            #if event.type == 

        # temp
        pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

        pygame.display.flip()
        
    def close(self):
        pygame.quit()

    def closing(self):
        return self.should_quit

g = Game()

try:
    while not g.closing():
        g.loop()
    py
