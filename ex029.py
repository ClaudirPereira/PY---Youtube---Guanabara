import math
print('.: DESAFIO 29 :.')
print('-' * 100)
print('Escreva um programa que leia a velocidade de um carro.\nSe ele ultrapassar 80km/h, mostre uma mensagem dizendo que foi multado.')
print('A multa vai custar R$ 7,00 por km acima do limite.')
print('-' * 100)
velocidade = int(input('Digite a velocidade do seu veículo: '))
print('.' * 100)
print(f'Sua Velocidade foi de {velocidade} km/h e o limite é de 80 km/h')
print('.' * 100)
if velocidade <= 80:
    print('Parabéns, siga com segurança! Não esqueça de usar o cinto de segurança!')
else:
    print(f'Você ultrapassou o limite de velocidade desta rodovia!\n>> Sua velocidade é de {velocidade:.0f}km/h.\n>> Sua multa é de R$ {(velocidade - 80) * 7:.2f}')
print('.' * 100)