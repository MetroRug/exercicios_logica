"""
 Crie um programa que leia o número de dias trabalhados em um mês e mostre o
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
por hora trabalhada.
"""
trabalhados = int(input("Total de dias trabalhados: "))
dia_trab = 25*8

print('O total recebido pelo funcionario é: R$', trabalhados*dia_trab)
