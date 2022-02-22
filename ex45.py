'''
45) O programa acima vai ter um problema quando digitarmos o primeiro valor
maior que o último. Resolva esse problema com um código que funcione em qualquer
situação.
'''

inicial = int(input('Diga o valor inicial: '))
final = int(input('Diga o valor final: '))
incremento = int(input('Diga o incremento: '))

def conta_positivo():
    for valor in range(inicial, final, incremento):
        print(valor)

def conta_negativo():
    for valor in range(inicial, final, -incremento):
        print(valor)

print('Contagem: ')

if inicial > final:
    conta_negativo()

else:
    conta_positivo()

print('Acabou!!')