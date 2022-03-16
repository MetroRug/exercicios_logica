'''
57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
No final, mostre o total de salários pagos aos homens e o total pago às
mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
sempre que ler os dados de um funcionário.
'''

#sexo = []
salario_masc = []
salario_fem = []

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

while True:
    condicao = input('Gostaria de adicionar um funcionário? [s]/[n] ')
    if condicao == 's':

        sexo = input('O funcionário(a) é homem ou mulher? ')

        if sexo == 'homem':
            int_salario_masc = float(input('Diga o vallor do sálario dele: '))
            salario_masc.append(int_salario_masc)
        elif sexo == 'mulher':
            int_salario_fem = float(input('Diga o vallor do sálario dela: '))
            salario_fem.append(int_salario_fem)

    elif condicao == 'n':
        break
    else:
        print('Por favor escolha ente [s] e [n]!')


soma_masc = somalista(salario_masc)
soma_fem = somalista(salario_fem)

print(f'Temos {len(salario_fem)} funcionárias, o salário total é de {soma_fem}.\n'
      f'Temos {len(salario_masc)} funcionários, o salário total é de {soma_masc}.')


