print('.: DESAFIO 13 :.')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')
n1 = float(input('Digite o Salário da Marlei: '))
print(f'O salário da Marlei é de R$ {n1:.2f}, sendo que ganhou 15% de aumento do patrãozinho e hoje o salário é de R${n1 + (15 * n1 / 100):.2f}. \n Teve um reajuste de R$ {15 * n1 / 100:.2f}')
