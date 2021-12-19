velocidade = float(input('Quantos quilometros o veiculo estava:'))

if velocidade>80:
    diferenca = velocidade-80
    multa = diferenca*5
    print(f'você ultrapassou a {diferenca}KM, sua multa foi de R${multa}')

else:
    print(f'Sua velocidade é de {velocidade}KM. DENTRO DO LIMITE')