print(' .: DESAFIO 14 :.')
print('Escreva um programa que converta uma temperatua digitada ºC e converta para ºF.')
c = float(input('Digite quantos ºC: '))
print(f'A temperatura informada é de {c}ºC sendo seu co-equivalente em {c * 1.8 + 32}ºF!') #a ordem de precedencia da multiplicação é a primeira que o sistema vai executar, a soma é a ultima ordem a ser executada sempre por isso não precisa dos ( ).
