'''import math
print('-' * 100)
print('.: DESAFIO 17')
print('-' * 100)
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule o comprimento da hipotenusa')
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hy = math.hypot(co, ca)
print('.' * 100)
print(f'A hipotenusa vai medir {hy:.2f}')
print('.' * 100)'''

from math import hypot
print('-' * 100)
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hy = hypot(co, ca)
print(f'A hipotenusa vai medir {hy:.2f}')
print('-' * 100)