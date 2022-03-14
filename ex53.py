'''
53) Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos
'''
grupo = []
homens = []
mulheres = []

i = 0
h = 0
m = 0
m_maior = 0

while i < 5:
    sexo = input('Qual o sexo? [H]/[M] ')
    sexo = sexo.upper()

    if sexo == 'H':
        idade_masc = int(input('Qual a idade dele? '))
        grupo.append(idade_masc)
        homens.append(idade_masc)
        h += 1

    elif sexo == 'M':
        idade_fem = int(input('Qual a idade dela? '))
        if idade_fem >= 20:
            m_maior += 1
        grupo.append(idade_fem)
        mulheres.append(idade_fem)
        m += 1

    else:
        print('Escolha entre H ou M.')
        continue

    i += 1

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

soma_idades_grupo = somalista(grupo)
media_grupo = soma_idades_grupo / len(grupo)

soma_idades_homens = somalista(homens)
media_homens = soma_idades_homens / len(homens)

print(f'Tivemos {h} homens cadastrados e {m} mulheres cadastradas.\n'
      f'A média de idade do grupo cadastrado é de {media_grupo} anos.\n'
      f'A média de idade dos homens cadastrados é de {media_homens} anos.\n'
      f'E temos {m_maior} mulheres com idade superior a 20 anos.')