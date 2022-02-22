"""
47) Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 +
450 + 400 + 350 + 300 + ... + 50 + 0
"""

n1 = 500
total = 0


while n1 >= 0:
    print(n1)
    n1 -= 50
    total += n1

    if n1 == 0:
        print(n1)
        break

print(total)
