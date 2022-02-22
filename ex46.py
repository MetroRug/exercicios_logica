'''
46) Crie um programa que calcule e mostre na tela o resultado da soma entre 6 +
8 + 10 + 12 + 14 + ... + 98 + 100.

'''

n1 = 0
total = 0


while n1 <= 100:
    print(n1)
    n1 += 2
    total+=n1

    if n1 == 100:
        print(n1)
        break

print(total)


