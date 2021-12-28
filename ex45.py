'''
45) O programa acima vai ter um problema quando digitarmos o primeiro valor
maior que o último. Resolva esse problema com um código que funcione em qualquer
situação.
'''

'''inicial = int(input('Diga o valor inicial: '))
final = int(input('Diga o valor final: '))
incremento = int(input('Diga o incremento: '))

n_incremento = -incremento

print()
print('Contagem:')

if inicial<final:
    
    for valor in range(inicial, final, incremento*-1):

        print(valor)

    print('Acabou!')

else:
    for valor in range(inicial, final, incremento):
        print(valor)

    print('Acabou!')
'''

print ("abs(-45) : ", abs(45))