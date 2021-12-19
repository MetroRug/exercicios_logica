"""
35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
 - Carros populares (aluguel de R$90 por dia)
 - Até 100Km percorridos: R$0,20 por Km
 - Acima de 100Km percorridos: R$0,10 por Km
 - Carros de luxo (aluguel de R$150 por dia)
 - Até 200Km percorridos: R$0,30 por Km
 - Acima de 200Km percorridos: R$0,25 por Km
"""

print('''
[0] Carro popular
[1] Carrol de luxo
''')

carro = int(input('Qual carro foi escolhido? '))
dia = int(input('Quantos dias o carro foi alugado? '))
quilometros = float(input('Quantos KM foram percorridos? '))

def aluguel_carro(aluguel,km_ex, taxa_km, taxa_ex):
    dia_usado = dia * aluguel
    if quilometros > km_ex:
        km_rodado = quilometros*taxa_ex
    else:
        km_rodado = quilometros * taxa_km

    return km_rodado + dia_usado

if carro == 0:
    resultado = aluguel_carro(90,100,0.20, 0.10)
    print(f'O valor do aluguel é de R$:{resultado:.2f}!')
elif carro == 1:
    resultado = aluguel_carro(150,200,0.30,0.25)
    print(f'O valor do aluguel é de R$:{resultado:.2f}!')
else:
    print("Escolha uma das opções 0 ou 1!")
