'''
58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
vai parar quando for digitada a idade 999. No final, mostre quantos alunos
existem na turma e qual é a média de idade do grupo.
'''
idades_turma = []

def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

while True:
    idade = int(input('Digite a idade do aluno: '))

    if idade == 999:
        break
    else:
        idades_turma.append(idade)

soma_idade= somalista(idades_turma)
media_idade = soma_idade / len(idades_turma)

print(f'Temos {len(idades_turma)} alunos na turma e a média de idade é de {media_idade:.2f} anos.')