'''
42) Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
qualquer e mostre uma contagem até esse valor:
Ex: Digite um valor: 35
Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!
'''
a = 1
b = int(input('Diga um número: '))

while a <= b:
    print(f'{a} ', end="")
    a += 1
print('Acabou!')