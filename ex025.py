print('.: DESAFIO 25 :.')
print('-' * 100)
#print('Crie um programa que leia  o nome de uma pessoa e diga se ela tem "SILVA" no nome.')
#nome = str(input('Digite o nome completo: ')).strip()
#print(f'Seu nome tem Silva? {"Silva" in nome.upper()}')
#nome = input('Digite seu nome completo: ').strip()
#i = nome.split()
#ver = i[0]
#confira = ('Silva'.title() in ver) or ('Silva'.lower() in ver) or ('SILVA' in nome.upper())
#z = (ver[0:][5:] in nome)
#print('Seu nome possui Silva? {}'.format(confira and z).replace('True', 'Sim').replace('False', 'Não'))
#nome = input('Digite seu nome completo: ').strip()
#i = nome.split()
#ver = i[0]
#confira = ('Silva'.title() in ver) or ('Silva'.lower() in ver) or ('SILVA' in nome.upper())
#z = (ver[0:][5:] in nome)
#print(f'Seu nome possui Silva? {confira and z}'.replace('True', 'Sim').replace('False', 'Não'))

nome = input('Digite seu nome completo: ')
idade = input('Digite sua idade: ')
sexo = input('Digite seu sexo: ')
pergunta01 = input('Você já roubou milho na beira da estrada?(s ou n) ')
ver = pergunta01[0]
confira = ('s'.title() in ver) or ('n'.title() in ver)
checagem = (ver[0:][3:]) in pergunta01
resposta1 = 'Você está de parabéns pois não é larápio!'
resposta2 = 'Você está de parabéns pois teve uma infância raiz!'
n = resposta1
s = resposta2
print(f' > Seu nome é {nome}.')
print(f' > Sua idade é {idade} anos. ')
print(f' > Seu sexo é {sexo}. ')
print(f' >>>> Status: {s or n}')
