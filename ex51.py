'''
51) Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela
qual foi o maior e qual foi o menor preço digitados.
'''
# 8.90, 4.75, 9.99, 3.70, 4.50, 2.35, 2.25, 11.99
valores_itens = []
i=0

while i < 8:
    valores = float(input('Diga o valor dos produtos: '))
    valores_itens.append(valores)

    i += 1

print(f'O menor valor da lista é {min(valores_itens)}.')
print(f'O maior valor da lista é {max(valores_itens)}.')
