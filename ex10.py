'''
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
'''

altura = float(input('Diga a altura: '))
largura = float(input('DIga a largura: '))

area = largura*altura

tinta = area/2

print(f'A parde possoi {area:.2f}M '
      f'E é necessario {tinta:.2f} litros')
