'''
6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10
'''
num = int(input('Diga um nomero: '))

ant = num - 1
sus = num + 1

print(f'o antecessor de {num} é {ant}.')
print(f'O sucessor de {num} é {sus}.')