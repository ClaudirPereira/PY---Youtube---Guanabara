print('.: DESAFIO 31 :.')
print('-' * 100)
print('Desenvolva um programa que pergunte a distância de uma viagem em km.\nCalcule o preço da passagem cobrando R$ 0,50 por km de viagem até 200 km\ne R$ 0,50 para viagens mais longas.')
print('-' * 100)
km = int(input('Digite a kilometragem: '))
print('.' * 100)
print(f'A sua viagem foi de {km} km')
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('.' * 100)
print(f'O preço da sua passagem será de R$ {preço:.2f}')