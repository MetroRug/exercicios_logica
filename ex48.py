'''
48) Faça um programa que leia 7 números inteiros e no final mostre o somatório
entre eles.
'''

n1 = 0
total = 0


while n1 <= 7:
    print(n1)
    n1 += 1

    total += n1

    if n1 == 7:
        print(n1)
        break

print(total)