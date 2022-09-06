print('.: DESAFIO 11 :.')
print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo. \n Sabendo que cada litro de tinta pinta uma área de 2m².')
n1 = float(input('Digite a altura: '))
n2 = float(input('Digite a largura: '))
print(f'Para pintar {n1 * n2}m² é necessário {n1 * n2 ** 1/2 } litros de tinta.') # posso usar também -> {(n1 * n2) / 2} <-
