print('.: DESAFIO 10 :.')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.')
print('Considerando US$ 1,00 = R$ 3,27')
n1 = float(input('Abra sua carteira, conte quantos reais você possui e digite aqui: R$ '))
print(f'Você com essa micharia de R${n1:.2f} pode comprar apenas US$ {n1 / 3.27:.2f}.')
