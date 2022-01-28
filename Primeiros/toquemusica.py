import pygame

pygame.init()
pygame.mixer.music.load('sambadinha.mp3')
pygame.mixer.music.play()
pygame.event.wait()