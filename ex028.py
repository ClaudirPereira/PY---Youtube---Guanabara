#import random
#print('.: DESAFIO 28 :.')
#print('-' * 100)
#print('Escreva um programa que faça o computador "pensar" em um número inteiro \nentre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.')
#print('  O programa deverá escrever na tela se o usuário venceu ou perdeu.')
#print('-' * 100)
#print(' .: Bem Vindo ao SHOW DO POBRÃO :.\n>> Aqui você acerta o número e não ganha nada <<\n-> SHOW DO POBRÃO <-')
#print('.' * 100)
#n = int(input('Digite um número de 0 á 5: '))
#print('.' * 100)
#lista = [0, 1, 2, 3, 4, 5]
#sorteado = random.choice(lista)
#print(f'O número que você apostou foi {n} e o número sorteado foi {sorteado}!')
#if n == sorteado:
#    print('** PARABÉNS ** \n** Você acertou o número sorteado do SHOW DO POBRÃO **')
#else:
#    print('** Você ERROU ** \n** Tente outra vez **')
#print('.' * 100)
from random import randint
from time import sleep #O comando sleep dentro do time, faz com que o programa espere um pouco e depois mostra na tela
computador = randint(0, 5) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número de 0 á 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('>> PARABÉNS!!! << \n>> Você conseguiu me vencer! <<')
else:
    print(f'>> GANHEI << \nEu pensei no número {computador} e eu você pensou no {jogador}.\n< TENTE OUTRA VEZ >')

