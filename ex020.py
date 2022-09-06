from random import shuffle

print('.: DESAFIO 20 :.')
print('-' * 100)
print('Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
print('-' * 100)
n1 = str(input('Primeiro Nome: '))
n2 = str(input('Segundo Nome: '))
n3 = str(input('Terceiro Nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('.' * 100)
print(f'A ordem de apresentação serão: \n {lista}')
print('.' * 100)