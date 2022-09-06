print('.: DESAFIO 24 :.')
print('-' * 100)
print('Crie um programa que leia o nome de uma cidade  e diga se ela começa ou não com o nome "SANTO".')
cid = str(input('Em que cidade você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')

#quando trabalhar com string..str... sempre colocar .strip() para eliminar os espaços indesejados,
# para que o programa use corretamente suas funções... optamos em transformar todas as letras em maiúsculas .upper()