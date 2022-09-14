import pygame
from UI import *

pygame.init()
resolution = [500,500]
screen = pygame.display.set_mode(resolution)


running=True

class Menu:
    def __init__(self):
        self.active = True

        self.bgcolor = (200,230,255)
        self.tImage=pygame.image.load('Assets/Images/Tetris_image.png')
       
        playButton=TextButton([100,275,300,50], (200,200,220), (55, 55, 55),'Play Game', pygame.font.SysFont('calibri', 25), True, False)
        optionsButton=TextButton([100,350,300,50],(200,200,220), (55, 55, 55), 'Options', pygame.font.SysFont('calibri', 25), True, False)
        exitButton=TextButton([175,425,150,50],(200,200,220), (55, 55, 55), 'Exit', pygame.font.SysFont('calibri', 25), True, False)

        self.buttonDict={
            "play": playButton,
            "options": optionsButton,
            "exit": exitButton
        }
    
    def checkButtons(self, mousePos):
        buttons = {
            "play": False,
            "options": False,
            "exit": False
        }

        for name in self.buttonDict:
            if self.buttonDict[name].check(mousePos):
                buttons[name] = True
        
        return buttons

    def render(self, screen):
        if not self.active:
            return

        screen.fill(self.bgcolor)
        screen.blit(self.tImage,(178,50))
        for name in self.buttonDict:
            self.buttonDict[name].render(screen)
        pygame.display.flip()

    def close(self):
        self.active = False
        pygame.mixer.music.stop()
