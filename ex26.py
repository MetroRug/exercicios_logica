n1 = int(input('Diga o primeiro número: '))
n2 = int(input('Diga o segundo número: '))

if n1 > n2:
    print(f'O primeiro número "{n1}" é maior que o segundo número "{n2}".')
elif n2 > n1:
    print(f'O segundo número "{n2}" é maior que o primeiro número "{n1}".')
else:
    print(f'O primeiro número "{n1}" é iqual ao segundo número "{n2}".')