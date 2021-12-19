"""
27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
 - Média até 4.9: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO
"""
nota1 = float(input('Diga a primeira nota: '))
nota2 = float(input('Diga a segunda nota: '))

media = (nota1 + nota2)/2

if media <=4.9:
    print(f'Média {media}:  Reprovado')
elif media >=5 and media <= 6.9:
    print(f'Média {media}:  RECUPERAÇÃO')
elif media >=7 and media <= 10:
    print('Média {media}:  APROVADO')