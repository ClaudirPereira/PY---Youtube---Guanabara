print('.: DESAFIO 37 :.')
print('-' * 100)
print('Faça um programa que leia o ano de alistamento, que informe a sua idade, se irá se alistar, se é a hora de se alistar, ou já excedeu o tempo do alistamento.')
print('-' * 100)
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Compareça imediatamente para o Alistamento Militar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta {saldo}')
    ano = atual + saldo
    print(f'Seu Alistamento Militar será no ano de {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se feito o Alistamento Militar á {saldo} anos.')
    ano = atual - saldo
    print(f'Seu Alistamento Militar foi em {ano}')
