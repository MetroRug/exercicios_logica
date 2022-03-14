'''
41) Desenvolva um programa que mostre na tela a seguinte contagem:
100 95 90 85 80 ... 0 Acabou!
'''

a = 100

while a >= 0:
    print(f'{a} ', end="")
    a -= 5
print('Acabou!')