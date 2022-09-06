print('.: DESAFIO 21 :.')
print('-' * 100)
print('Faça um programa em python que abra e reproduza um áudio de um arquivo mp3.')
print('-' * 100)
import pygame
#inicia o mixer primeiro
pygame.mixer.init()
#inicia o pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0)
pygame.event.wait()
