'''
49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles
são pares e quantos são ímpares.

'''
n1 = 0
total_par = 0
total_impar = 0

while n1<6:
    n2 = int(input('Digite um número: '))
    if n2%2 == 0:
        total_par += 1
    else:
        total_impar += 1
    n1 += 1

print(f'De {n1} números, temos {total_par} números pares e {total_impar} números impares')