import time
import pygame
from random import *
from GameWindow import *
from Menu import *
from SoundHandler import Tracks
from dataclasses import dataclass

@dataclass
class KeyState:
    state: bool
    should_reset: bool

##game is designed for a square window

# runtime variables
resolution = [500,500]
screen = pygame.display.set_mode(resolution)

flags = {
    "gameOver": False,
    "lineClear": False,
    "tetris": False,
    "wallHit": False
}

time_elapsed = 0
clock = pygame.time.Clock()
FPS = 15

running = True

#Music handler
music_tracks = Tracks(8)
Menu_music = pygame.mixer.Sound("Assets/Music/Menu_music.wav")
Gameplay_music = pygame.mixer.Sound("Assets/Music/Gameplay_music.wav")
Game_over = pygame.mixer.Sound("Assets/Music/Game_over.wav")
Wall_hit = pygame.mixer.Sound("Assets/Music/Wall_hit.wav")
Line_cleared = pygame.mixer.Sound("Assets/Music/Line_cleared.mp3")

#UI elements
game = GameWindow(resolution, flags)
menu = Menu()

# inputs Format .active, .should_reset
keys = {
    pygame.K_LEFT: KeyState(False, False),
    pygame.K_RIGHT: KeyState(False, False),
    pygame.K_DOWN: KeyState(False, False),
    pygame.K_d: KeyState(False, True),
    pygame.K_a: KeyState(False, True)
}

# mainloop
music_tracks.playSound(Menu_music, -1)
while running:
    time_start = time.perf_counter()

    # rendering
    game.render(screen)
    menu.render(screen)
    pygame.display.flip()

    # events and flags
    game.update(time_elapsed)
    game.userInput(keys)

    if flags["gameOver"]:
        flags["gameOver"] = False
        game.render(screen)
        music_tracks.stopSound(Gameplay_music)
        music_tracks.playSound(Game_over, 0)
        game.active = False
        time.sleep(2)
        running = False
    
    if flags["wallHit"]:
        flags["wallHit"] = False
        music_tracks.playSound(Wall_hit, 0)

    if flags["lineClear"]:
        flags["lineClear"] = False
        music_tracks.playSound(Line_cleared, 0)


    # input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key].state = True

        elif event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key].state = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons = menu.checkButtons(pygame.mouse.get_pos())
            if buttons["play"]:
                menu.close()
                music_tracks.stopSound(Menu_music)
                music_tracks.playSound(Gameplay_music, -1, 0.2)
                game.start()

    clock.tick(FPS)
    time_end = time.perf_counter()
    time_elapsed = time_end-time_start

pygame.quit()