print('.: DESAFIO 33 :.')
print('-' * 100)
print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# menor = a >> to estimando que o a seria o menor valor... mas se não for então... b<a e (and) b<c... o menor será o b // a mesma coisa acontece com o c.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor é {menor} e o valor maior é {maior}')
