"""
29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20%
"""
nome = input('Diga o nome do funcionario: ')
salario = float(input('Salário atual do funcionário: R$ '))
anos = int(input('Anos trabalhados: '))

def percentual(perc):
    return salario + ((perc/100)*salario)

if anos < 3:
    novo_salario = percentual(3)
    print(f'O funcionário {nome} trabalhou por {anos} anos, seu salário atual é de R$:{novo_salario}')
elif anos >= 3 and anos<=10:
    novo_salario = percentual(12.5)
    print(f'O funcionário {nome} trabalhou por {anos} anos, seu salário atual é de R$:{novo_salario}')
else:
    novo_salario = percentual(20)
    print(f'O funcionário {nome} trabalhou por {anos} anos, seu salário atual é de R$:{novo_salario}')
