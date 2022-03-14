'''
54) Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando
no final:
a) Qual foi a média de altura do grupo
b) Quantas pessoas pesam mais de 90Kg
c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.
'''

altura = []
peso = []

i = 0

n_peso = 0
n_altura = 0
c_altura_peso = 0
d_altura_peso = 0

while i < 3:
    int_altura = float(input('Qual a altura? '))
    altura.append(int_altura)

    int_peso = int(input('Qual o peso? '))
    peso.append(int_peso)

    if int_peso > 90:
        n_peso += 1
    elif int_peso < 50 and int_altura < 1.60:
        c_altura_peso += 1
    elif int_peso > 100 and int_altura > 1.90:
        d_altura_peso += 1

    i += 1

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

soma_altura = somalista(altura)
media_altura = soma_altura / len(altura)

print(f'A média de altura do  grupo é de {media_altura:.2f} metros.\n'
      f'{n_peso} pessoas pesam mais de 50 KG.\n'
      f'{c_altura_peso} pessoas pesam menos de 50Kg tem menos de 1.60m\n'
      f'{d_altura_peso} pessoas medem mais de 1.90m pesam mais de 100Kg.')