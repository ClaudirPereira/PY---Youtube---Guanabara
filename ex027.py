print('.: DESAFIO 27 :.')
print('-' * 100)
print('Faça um programa que leia  o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.')
print('-' * 100)
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Satisfação em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[-1]}')
# o numero 0 diz que ele vai começar da esquerda pra direita,
#o -1 indica q vai começa da direita pra esquerda.