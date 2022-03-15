'''
8) Desenvolva um programa que leia uma distância em metros e mostre os valores
relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72
A distância de 85.7m corresponde a:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
'''

distm = float(input('Digite uma distância em metros: '))

print (distm / 1000, 'KM')
disthm = distm / 100
distdam = distm / 10
distdm = distm * 10
distcm = distm * 100
distmm = distm * 1000

print(f'A distância de {distm}M corresponde a: \n'
      #f'{distkm} KM\n'
      f'{disthm} HM\n'
      f'{distdam} DAM\n'
      f'{distdm} DM\n'
      f'{distcm} CMz\n'
      f'{distmm} MM')

