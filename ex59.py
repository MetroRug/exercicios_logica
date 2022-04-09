'''
59) Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
a) qual é a maior idade lida
b) quantos homens foram cadastrados
c) qual é a idade da mulher mais jovem
d) qual é a média de idade entre os homens
'''
homens_idade = []
mulheres_idade = []

while True:
    continua = input('Gostaria de cadastrar uma pessoa? [s]/[n] ')
    if continua == 's':
        sexo = input('Qual o sexo da pessoa? [h]/[m] ')
        if sexo == 'h':
            idade = int(input('Diga a idade dele: '))
            homens_idade.append(idade)
        elif sexo == 'm':
            idade = int(input('Diga a idade dela: '))
            mulheres_idade.append(idade)
    else:
        break

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

soma_idade = somalista(homens_idade)
media_idade = soma_idade / len(homens_idade)


todas_listas = homens_idade + mulheres_idade
print(f'\n\nA maior idade lida é {max(todas_listas)} anos.\n'
      f'Tivemos {len(homens_idade)} homens registrados.\n'
      f'A mulher mais jovem registrada tem {min(mulheres_idade)} anos.\n'
      f'A média de idade dos homens cadastrados é de {media_idade:.2f} anos.')

