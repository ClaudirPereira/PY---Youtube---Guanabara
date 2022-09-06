print('.: DESAFIO 12 :.')
print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.')
n1 = float(input('Insira o valor do produto: R$ '))
print(f'A sua compra de R$ {n1:.2f} teve um desconto de 5% e vai custar R$ {n1 - (n1 * 5 / 100):.2f}. \nTotalizando R$ {(5 * n1) / 100:.2f} em desconto.')
