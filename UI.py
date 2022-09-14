import pygame

class Label:
    #shared properties for any Label
    def __init__(self, bgColor, texture, rect, visible=True):
        self.texture = texture
        self.bgColor = bgColor
        self.rect = rect
        self.visible = visible
    
    def render(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.bgColor, self.rect, 0)
            surface.blit(self.texture, (self.rect[0], self.rect[1]))

class TextLabel(Label):
    def __init__(self, bgColor, font, text, text_color, rect, visible=True):
        self.font = font
        texture = font.render(text, True, text_color)
        super().__init__(bgColor, texture, rect, visible)
    
    def changeText(self, text_color, text):
        self.texture = self.font.render(text, True, text_color)

class Button(Label):
    def __init__(self, bgColor, texture, rect, visible=True, toggleable=False):
        super().__init__(bgColor, texture, rect, visible)
        self.toggleable = toggleable
        self.state = False

    def check(self, mousePos):
        x, y, w, h = self.rect
        if not self.visible:
            return
        if (x <= mousePos[0] <= x+w) and (y <= mousePos[1] <= y+h):
            if self.toggleable:
                self.state = not self.state
            else:
                return True
        return self.state

class TextButton(Button):
    def __init__(self, rect, bgColor, text_color, text, font, visible=True, toggleable=False):
        self.font = font
        texture = font.render(text, True, text_color)
        super().__init__(bgColor, texture, rect, visible, toggleable)

    def changeText(self, text_color, text):
        self.texture = self.font.render(text, True, text_color)