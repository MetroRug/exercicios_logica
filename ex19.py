"""
 Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
não um bom aproveitamento (se ficou acima da média 7.0).
"""

aluno = input("Diga o nome do aluno: ")
nota1 = float(input('Diga a primeira nota: '))
nota2 = float(input('Diga a segunda nota: '))

media = (nota1 + nota2)/2

print(f'\n{aluno} teve uma média de {media}')

if media>7:
    print(f'{aluno} teve um bom aproveitamento.')
else:
    print(f'{aluno} não teve um bom aproveitamento.')