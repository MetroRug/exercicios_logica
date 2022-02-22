'''
49) Crie um programa que leia 6 números inteiros e no final mostre quantos deles
são pares e quantos são ímpares.

'''

n1 = 0
n2 = n1%2
total_par = 0
total_impar = 0

while n1 <= 6:
    n1 += 1
    if n2 == 0:
        total_par += 1
    else:
        total_impar += 1

print(f"Temos {total_par} números pares e {total_impar} números impares.")