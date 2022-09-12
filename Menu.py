import pygame

pygame.init()
resolution = [500,500]
screen = pygame.display.set_mode(resolution)


running=True

class Button:
    def __init__(self,x,y,w,h,t,col,font,fontSize,function):
        self.w=w
        self.h=h
        self.text=t
        self.x=x
        self.y=y
        self.col=col
        self.fontName=font
        self.fontSize=int(fontSize)
        self.font=pygame.font.SysFont(self.fontName, self.fontSize)
        self.selected=False
        self.function=function
        

    def render(self, screen):
        pygame.draw.rect(screen, self.col, (self.x, self.y, self.w, self.h))
        renderText=self.font.render(self.text, True, [0,0,0])
        textRect=renderText.get_rect(center=(500/2, self.y+25))
        screen.blit(renderText, textRect)

    def isSelected(self,mouse):
        self.selected=False
        if self.x<=mouse[0]<=self.x+self.w and self.y<=mouse[1]<=self.y+self.h:
            self.selected=True
            if self.function=='e':
                pygame.quit()
            #elif self.function=='p':
                #play game
            #elif self.function=='o':
                #options menu

class Menu:
    def __init__(self):
        self.active = True

        self.bgcolor = (200,230,255)
        self.tImage=pygame.image.load('Assets/Images/Tetris image.png')
       
        playButton=Button(100,275,300,50,'Play Game',(200,200,220),'calibri',25,'p')
        optionsButton=Button(100,350,300,50,'Options',(200,200,220),'calibri',25,'o')
        exitButton=Button(175,425,150,50,'Exit',(200,200,220),'calibri',25,'e')

        self.buttonList=[playButton,optionsButton,exitButton]

    def menuMusic(self):
        pygame.mixer.music.load("Assets/Music/Menu music.wav")
        pygame.mixer.music.play(-1)

    def render(self, screen):
        screen.fill(self.bgcolor)
        screen.blit(self.tImage,(178,50))
        for button in self.buttonList:
            button.render()
        pygame.display.flip()

    def close(self):
        self.active = False
        pygame.mixer.music.stop()
