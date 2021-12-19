ano_nas = int(input('Diga seu ano de nascimento: '))

idade = 2021 - ano_nas

if idade >= 18:
    print('Sim, tem idade para votar!')

else:
    print('Não, não tem idade para votar.')