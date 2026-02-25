import pygame
pygame.init()
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play()
pygame.event.wait()