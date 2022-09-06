print('.: DESAFIO 26 :.')
print('-' * 100)
print(' Faça um programa que leia uma frase  pelo teclado  e mostre: \n >> Quantas vezes aparece a letra A. \n >> Em quantas posições ela aparece a primeira vez. \n >> Em que posição ela aparece a ultima vez.')
print('-' * 100)
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")} vezes.')
print(f'A primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'A última letra A apareceu na posição {frase.rfind("A")+1}')
#o +1 faz a adequação da primeira posição numérica... pois o python entende que começa pelo numero 0 e com o +1 nós damos informação pra ele achar a partir do+1