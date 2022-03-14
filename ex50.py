'''
50) Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e
mostre na tela:
a) Quais foram os números sorteados
b) Quantos números estão acima de 5
c) Quantos números são divisíveis por 3
'''
import random

numeros = 0
numeros_sorteio = []
numeros_acima = 0
numeros_divisao = 0

while numeros < 20:
    sorteio = random.randrange(0, 10, 1)
    numeros_sorteio.append(sorteio)
    numeros += 1

    if sorteio > 5:
        numeros_acima += 1
    elif sorteio%3==0:
        numeros_divisao += 1

print(f'Números do sorteio: {numeros_sorteio}')
print(f'Temos {numeros_acima} acima de 5.')
print(f'Temos {numeros_divisao} divisiveis por 3.')


