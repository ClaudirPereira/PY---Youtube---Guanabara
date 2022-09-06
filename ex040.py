print('.: DESAFIO 40 :.')
print('-' * 100)
print('Crie um programa que leia duas notas de um aluno e calcule sua média\nmostrando uma mensagem no final deacordo com a média obtida:')
print('- Média abaixo de 5.0: REPROVADO\n- Média entre 5.0 e 6.9: RECUPERAÇÃO\n- Média 7.0 ou Superior: APROVADO')
print('-' * 100)
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
média = (n1 + n2) / 2
if média < 5:
    print(f'A sua média foi{média} e você foi REPROVADO!')
elif 7 > média >= 5:
    print(f'A sua média foi {média} e você esta em RECUPERAÇÃO!')
elif média >= 7:
    print(f'A sua média foi {média} e você está APROVADO!')
#elif 7 > média >= 5: -- senão se 7 é o mínimo pra aprovar... e sua média for menor que 7 e maior q 5.. recuperação