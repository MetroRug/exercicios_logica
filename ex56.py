'''
56) Crie um programa que leia vários números pelo teclado e mostre no final o
somatório entre eles.
Obs: O programa será interrompido quando o número 1111 for digitado
'''

numeros = []

while True:
    con = int(input('Diga um número inteiro: '))
    numeros.append(con)

    info = input('Deseja continuar? [S]/[N]')
    info = info.upper()

    if info == 'S':
        continue
    elif info =='N':
        break
    else:
        print('Escolha entre S ou N.')


def somalista(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma

print(f'A soma dos números é igual a {somalista(numeros)}')