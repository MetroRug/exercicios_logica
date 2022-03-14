'''
52) Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
a) Qual é a média de idade do grupo
b) Quantas pessoas tem mais de 18 anos
c) Quantas pessoas tem menos de 5 anos
d) Qual foi a maior idade lida
'''


idades = [10, 18, 22, 55, 42, 1, 5, 90, 38, 50]
acima18 = 0
abaixo5 = 0

# Calculo da media
def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

soma_idades = somalista(idades)
media = soma_idades / len(idades)

# Diferença de idades
for i in idades:
    if i >= 18:
        acima18 += 1
    elif i <= 5:
        abaixo5 += 1

print(f'A média de idade do grupo é de {media} anos \n'
      f'Temos {acima18} pessoas acima dos 18 anos e {abaixo5} pessoas abaixo dos 5 anos. \n'
      f'A maior idade do grupo é de {max(idades)} anos.')