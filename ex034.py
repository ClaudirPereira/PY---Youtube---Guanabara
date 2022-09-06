print('.: DESAFIO 34 :.')
print('-' * 100)
print('Escreva um programa que pergunte um salário e calcule o valor do seu aumento.')
print('Para salários superiores á R$ 1.250,00, calcule o aumento de 10%.')
print('Para salários inferiores o iguais, o aumento é de 15%.')
salario = float(input('Digite o seu salário: R$ '))
#salario vezes (*) 15 / 100 (15%) // para dar desconto é só substituir o + pelo -
if salario >= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'Quem ganhava R$ {salario:.2f} hoje está ganhando R$ {novo:.2f}')