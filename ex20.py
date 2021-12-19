"""
Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
ÍMPAR.
"""

numero = int(input("diga um numero: "))
resto = numero % 2

if resto == 0:
    print('Número é par.')
else:
    print('Número é impar.')