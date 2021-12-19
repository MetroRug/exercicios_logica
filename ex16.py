"""
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.
"""
ano = 365
quant_cigarros_dia = int(input('cigarros fumados por dia: '))
anos_fumados = int(input('Anos fumados: '))

total = quant_cigarros_dia * anos_fumados * ano

print(f'A quantidade de cigarros qie você fumou durante {anos_fumados} anos é de {total}')

tempo = total*10
hora = tempo/1440

print(f'A quantidade de dias perdidos foram {hora:.0f} dias.')
