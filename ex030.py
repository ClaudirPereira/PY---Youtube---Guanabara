print('.: DESAFIO 30 :.')
print('-' * 100)
print('Crie um programa que leia um número inteiro e mostre na tela se é PAR ou ÍMPAR.')
n = int(input('Digite um número: '))
print('-' * 100)
print(f'Seu número digitado foi {n}.')
print('Analisando o número escolihdo...')
print('.' * 100)
if n % 2 == 0:
    print(f'>> O número escolhido foi {n} e ele é PAR <<')
else:
    print(f'> O número escolhido foi {n} e ele é ÍMPAR <')
print('.' * 100)