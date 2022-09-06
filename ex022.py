print('.: DESAFIO 22 :.')
print('-' * 100)
print('Crie um programa que leia o nome completo de uma pessoa e mostre:')
print('>> O nome com todas as letras maiúsculas e minúsculas. \n >> Quantas letras ao todo (sem considerar espaços). \n >> Quantas letras tem o primeiro nome.')
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.')
print(f'Quantas letras tem o primeiro nome {nome.find(" ")}')

#strip elimina os espaços
#find procura algo... no calso procura dentro do nome quantas letras tem
