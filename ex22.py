"""
Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar.
 - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
alistamento.
 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
alistamento.
"""

ano = int(input('Diga o seu ano de nascimento:'))
idade = 2021 - ano

if idade < 18:
    anos_alist = 18 - idade
    print(f'Falta {anos_alist} anos para você se alistar.')
else:
    anos_alist = idade - 18
    print(f'Você passou {anos_alist} anos do prazo de alistamento.')

