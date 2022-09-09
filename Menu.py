import pygame

pygame.init()
resolution = [500,500]
screen = pygame.display.set_mode(resolution)
bgcolor = (255, 255, 0)

running=True

class Button:
    def __init__(self,x,y,w,h,t,col,font,fontSize):
        self.w=w
        self.h=h
        self.text=t
        self.x=x
        self.y=y
        self.col=col
        self.fontName=font
        self.fontSize=int(fontSize)
        self.font=pygame.font.SysFont(self.fontName, self.fontSize)
        

    def render(self, screen):
        pygame.draw.rect(screen, self.col, (self.x, self.y, self.w, self.h))
        renderText=self.font.render(self.text, True, [30, 30, 155])
        screen.blit(renderText, (self.x, self.y))


def Menu():
    screen.fill(bgcolor)
    playButton.render(screen)
    pygame.display.flip()
    #menuMusic()

#def menuMusic():
#    pygame.mixer.music.load("Menu music.wav")
#    pygame.mixer.music.play(-1)


playButton=Button(100,250,300,50,'Play Game',(55,55,55),'bell.tff',25)

optionsButton=Button(100,350,300,50,'Options',(55,55,55),'bell.tff',25)


while running:
    Menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
