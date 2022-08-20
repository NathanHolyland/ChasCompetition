import pygame
from PIL import Image

class Label:
    #shared properties for any Label
    def __init__(self, bgColor, texture, rect, visible):
        self.texture = texture
        self.bgColor = bgColor
        self.rect = rect
        self.visible = visible
    
    def draw(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.color, self.rect, 0)
            surface.blit(self.texture, (self.rect[0], self.rect[1]))

class ImageLabel(Label):
    def __init__(self, rect, visible, image):
        self.texture = pygame.image()


class TextButton(Label):
    def __init__(self, bgColor, text_color, font, text, rect, visible, toggleable):
        self.font = font
        texture = font.render(text, True, text_color)
        super().__init__(bgColor, texture, rect, visible)
        self.toggleable = toggleable
        self.state = False

    def changeText(self, text_color, text):
        self.texture = self.font.render(text, True, text_color)

    def check(self, mousePos):
        x, y, w, h = self.rect
        if self.visible:
            if (x <= mousePos[0] <= x+w) and (y <= mousePos[1] <= y+h):
                if self.toggleable:
                    self.state = not self.state
                else:
                    return True
        return self.state