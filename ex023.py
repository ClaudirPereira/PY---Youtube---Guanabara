print('.: DESAFIO 23 :.')
print('-' * 100)
print('Faça um programa que leia um número de 0 á 9999 e mostre na tela cada um dos dígitos separados.')
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

# peguei no valor do numero num, fiz a divisão inteira //, pela unidade 1, tirei o módulo o resto da divição por 10>> % 10
# depois so alterei em dezena, centena e milhar.