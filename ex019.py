import random
print('.: DESAFIO 19')
print('-' * 100)
print('Um professor  quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o  nome deles e escolhendo o nome escolhido.')
print('-' * 100)
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('.' * 100)
print(f'Os nomes inscritos para o sorteio foram: \n {n1} \n {n2} \n {n3} \n {n4} \n E o nome sorteado foi >> {escolhido} <<')