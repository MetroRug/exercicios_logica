"""
Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
para todos, mas especialmente para mulheres. Faça um programa que leia nome,
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
que:
 - Homens ganham 5% de desconto
 - Mulheres ganham 13% de desconto
"""

nome = input("Diga seu nome: ")
sexo = input("Diga seu sexo: [H/M]")
valor = float(input("Valor da compra: "))



if sexo == 'M':
    desc = valor * 13 /100
    valor_final = valor - desc
    print(valor_final)

elif sexo == 'H':
    desc = valor * 5 / 100
    valor_final = valor - desc
    print(f'{nome}, sua compra é de R${valor_final}.')

else:
    print('Favor escolher uma opção valida: [H/M]')
