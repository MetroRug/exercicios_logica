'''
40) Crie um aplicativo que mostre na tela a seguinte contagem:
0 3 6 9 12 15 18 Acabou!
'''

a = 0


while a <= 18:
    print(f'{a} ', end="")
    a += 3
print('Acabou!')