'''
13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
'''

produto = float(input('Diga o valor do salário: '))


valor_total = produto*15/100
novo_valor = produto+valor_total

print(f'O valor do salário é R${novo_valor}')