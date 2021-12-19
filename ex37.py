'''
37) Uma empresa precisa reajustar o salário dos seus funcionários, dando um
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
No final, mostre o seu novo salário, baseado na tabela a seguir:
- Mulheres
 - menos de 15 anos de empresa: +5%
 - de 15 até 20 anos de empresa: +12%
 - mais de 20 anos de empresa: +23%
- Homens
 - menos de 20 anos de empresa: +3%
 - de 20 até 30 anos de empresa: +13%
 - mais de 30 anos de empresa: +25%
'''
anos = int(input('Quantos anos o funcionário(a) tem de firma? '))
genero = input('Qual o sexo do funcionário(a)? ')
salario_atual = float(input('Qual o sálario atual? '))
genero = genero.upper()

def novo_salario(porcentagem):

    valor_novo = salario_atual+(salario_atual*(porcentagem/100))
    print(f'R$ {valor_novo:.2f}')

if genero == 'MULHER' or genero == 'M' or genero == 'FEMININO':
    print('O novo salário da funcionária é de ', end='')
    if anos < 15:
        novo_salario(5)
    elif anos > 15 or anos < 20:
        novo_salario(12)
    else:
        novo_salario(23)
elif genero == 'HOMEM' or genero == 'H' or genero == 'MASCULINO':
    print('O novo salário do funcionário é de ', end='')
    if anos < 15:
        novo_salario(3)
    elif anos > 15 or anos < 20:
        novo_salario(13)
    else:
        novo_salario(25)
else:
    print('Selecione uma opção valida!')