from datetime import date
print('.: DESAFIO 32 :.')
print('-' * 100)
print('Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.')
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')

# and ano % 100 != 0 >> e também (and) ano divisível (%) por 100 e não pode ser diferente de 0 (!=)
# or ano % 400 == 0 >> ou então (or) ano ser divisível (%) por 400 igual a 0 (==)
# from datetime import date >> importei a biblioteca datetime e utilizei somene a data
# ano = date.today().year >> vai pegar o ano atual da maquina.
