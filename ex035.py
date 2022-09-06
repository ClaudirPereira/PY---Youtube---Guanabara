print('.: DESAFIO 35 :.')
print('-' * 50)
print('Desenvolva um programa que leia o comprimento \nde três retas e diga ao usuário \nse elas podem ou não formar um triângulo.')
print('-=' * 25)
print('Analizador de triângulos')
print('-=' * 25)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos a cima NÃO PODEM FORMAR UM TRIÂNGULO!')

