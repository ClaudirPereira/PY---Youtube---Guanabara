print('.: DESAFIO 37 :.')
print('-' * 100)
print('Escreva um programa que leia um número inteiro e peça para o usuário para escolher qual será a base de conversão.')
print('- 1 Binário\n- 2 Octal\n- 3 hexadecimal')
print('-' * 100)
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('** OPÇÃO INVÁLIDA! Tente Novamente **')
#no final do {bin oct hex(num), foi colocado o fatiamento [2:], que inicia a partir do 3º número q lembrando q conta 0, 1, 2.
