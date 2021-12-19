"""
28) Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista abaixo:
 - Abaixo de 100m² = TERRENO POPULAR
 - Entre 100m² e 500m² = TERRENO MASTER
 - Acima de 500m² = TERRENO VIP
"""
largura = float(input('Diga a largura do terreno (em metros): '))
comprimento = float(input('Diga o comprimento do terreno (em metros): '))

a = largura * comprimento

if a < 100:
    print(f'Terreno com {a} metros quadrados. (TERRENO POPULAR)')
elif a >= 100 and a < 500:
    print(f'Terreno com {a} metros quadrados. (TERRENO MASTER)')
else:
    print(f'Terreno com {a} metros quadrados. (TERRENO VIP)')