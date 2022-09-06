print('.: DESAFIO 38 :.')
print('-' * 100)
print('Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:')
print('- O Primeiro valor é maior.\n- O Segundo valor é menor.\n- Não existe valor maior, os dois são iguais.')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é maior.')
else:
    print('Os valores são iguais.')
