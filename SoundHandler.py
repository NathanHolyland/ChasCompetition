import pygame

class Tracks:
    def __init__(self, channel_limit):
        pygame.mixer.init(channels=channel_limit)
    
    def playSound(self, sound_object, loops, volume=1):
        for channel in range(pygame.mixer.get_num_channels()):
            if pygame.mixer.Channel(channel).get_busy():
                continue
            sound_object.set_volume(volume)
            pygame.mixer.Channel(channel).play(sound_object, loops)
            return
        print("All channels are busy, consider initalising with > channel_limit")
    
    def stopSound(self, sound_object):
        for channel in range(pygame.mixer.get_num_channels()):
            if pygame.mixer.Channel(channel).get_sound() == sound_object:
                pygame.mixer.Channel(channel).stop()
