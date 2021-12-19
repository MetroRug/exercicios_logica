"""
A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
"""

km_rodados = float(input('Quantos km o carro rodou: '))
dias = int(input('Quantidade de dias: '))

precokm =0.20*km_rodados
total_dias = 90 * dias
total = precokm + total_dias

print(f'Total a pagar é de R${total}')

