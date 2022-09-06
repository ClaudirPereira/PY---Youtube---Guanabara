'''print('.: DESAFIO 16 :.')
print('.' * 100)
print('Crie um programa que leia o número Real qualquer pelo teclado e mostre na tela a sua porção inteira. ')
n1 = float(input('Digite um número: '))
from math import trunc
print(f'O valor digitado foi {n1} e a sua porção inteira é {trunc(n1)}')
print('.' * 100)'''

n1 = float(input('Digite um número: '))
print(f'O valor diitado foi {n1} e a sua porção inteira é {int(n1)}')