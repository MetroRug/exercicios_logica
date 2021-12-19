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

