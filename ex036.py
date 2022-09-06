print('.: DESAFIO 36 :.')
print('-' * 100)
print('Escreva um programa de aprovação bancário. Pergunte o valor da casa, o salário, quantos anos vai pagar.\nA prestação mensal, não pode exceder 30% do salario.')
print('-' * 100)
imovel = float(input('Digite o valor do imóvel: R$ '))
salario = float(input('Digite o seu salário: R$ '))
anos = int(input('Digite quantos anos vai pagar: '))
prestacao = imovel / (anos * 12)
mínimo = salario * 30 / 100
print(f'Para pagar uma casa de R$ {imovel:.2f} em {anos} anos, a prestação será de R$ {prestacao:.2f}')
if prestacao <= mínimo:
    print('Emprestimo APROVADO:')
else:
    print('Emprestimo NEGADO:')

#a prestação eu peguei a quantidade de anos vezes 12 meses vai dar o tempo da prestação em meses. ai eu dividi o valor da casa pela prestação