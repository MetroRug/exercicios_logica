"""
34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
indivíduo dentro de certas faixas.
 - abaixo de 18.5: Abaixo do peso
 - entre 18.5 e 25: Peso ideal
 - entre 25 e 30: Sobrepeso
 - entre 30 e 40: Obesidade
 - acima de 40: Obseidade mórbida
Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado
da altura)
"""

peso = int(input('Diga seu peso em KG: '))
altura = float(input('Diga sua altura em metros: '))
#altura_em_metros = altura/100

fodase = peso/(altura*altura)


if fodase <= 18.5 or fodase == 25:
    print(f'Seu IMC é de {fodase:.2f}. Você tem um peso ideal!')
elif fodase > 25 or fodase == 30:
    print(f'Seu IMC é de {fodase:.2f}. Você tem sobrepeso!')
elif fodase > 30 or fodase == 40:
    print(f'Seu IMC é de {fodase:.2f}. Você tem Obesidade!')
elif fodase > 40:
    print(f'Seu IMC é de {fodase:.2f}. Você tem Obseidade mórbida!')
else:
    print('ERRO')