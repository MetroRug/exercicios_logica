"""
33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
salario = float(input('Qual o seu salário? \n'))
valor_casa = float(input('qual é o valor da casa? \n'))
anos = int(input('Em quantos anos serão pagos? \n'))

prestacao = valor_casa/anos
prestacao_mes = prestacao/24
porcentagem = salario + ((30/100)*salario)

if prestacao_mes > porcentagem:
    print('Empréstimo bancário negado!')
else:
    print('Empréstimo bancário aceito!')