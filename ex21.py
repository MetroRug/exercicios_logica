ano = int(input('Diga o ano:'))
resto = ano%4

if resto == 0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto')
