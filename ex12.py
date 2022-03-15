'''
12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto.
'''

produto = float(input('Diga o valor do produto: '))


valor_total = produto*5/100
novo_valor = produto-valor_total

print(f'O valor do prtudo com desconto é R${novo_valor}')