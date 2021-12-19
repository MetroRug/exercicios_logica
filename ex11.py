import math

a = float(input('Diga a variavel A: '))
b = float(input('Diga a variavel B: '))
c = float(input('Diga a variavel C: '))

delta = (b*b)-(4*a*c)

if delta <= 0:
    print('ERRO VADIA')
else:
    x1 = ((-b + (math.sqrt(delta))) / (2 * a))
    x2 = ((-b+(math.sqrt(delta)))/ (2*a))
    print(f'Valor de x1 é: {x1}\n'
          f'Valor de x1 é: {x2}')
