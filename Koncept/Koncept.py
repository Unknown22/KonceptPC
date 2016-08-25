import pygame, sys
import time

from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()

        width = 750
        height = 700
        self.screen = pygame.display.set_mode((width,height))
        self.DISPLAYSURF = pygame.Surface(self.screen.get_size())
        self.DISPLAYSURF = self.DISPLAYSURF.convert()

        pygame.display.set_caption('Koncept')


        self.board1 = pygame.image.load('img/board1-750x700.jpg').convert()
        self.board2 = pygame.image.load('img/board2-750x700.jpg').convert()

        self.kleo = pygame.image.load('img/kleo.jpg').convert()
        self.tlo = pygame.image.load('img/tlo.jpg').convert()
        self.napis = pygame.image.load('img/napis.jpg').convert()

        self.screen.fill((0,0,0))
        self.screen.blit(self.tlo, (0,0))

        pygame.display.flip()

    def splash(self):
        self.screen.set_colorkey((255,0,255))
        self.screen.blit(self.tlo, (0,0))
        self.screen.blit(self.napis, (self.screen.get_rect().centerx,0))
        pygame.display.flip()
        self.start()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.screen.blit(self.board2, (0,0))
                        pygame.display.flip()
                    elif event.key == K_LEFT:
                        self.screen.blit(self.board1, (0,0))
                        pygame.display.flip()

if __name__=="__main__":
    game = Game()
    game.splash()