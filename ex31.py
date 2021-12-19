# 31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
from random import randint
#importar o módulo time para cadenciar o nome JÔKEMPO
from time import sleep

#definindo os itens
itens = ('Pedra', 'Papel', 'Tesoura')

#jogada do computador
computador = randint(0,2)

#apresentar as informações
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')

#agora o jogador faz a jogada
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ')
sleep(2)
print('-='*11)

"""conta as jogadas
perdeu = 3
ganhou = 0"""

#mostrando o que cada um jogou
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-='*11)



#montar estruturas condicionais para apresentar os resultados
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('jogada inválida!')

elif computador == 1: #computador jogou Papel
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    elif jogador == 0:
        print('JOGADOR PERDEU')
    else:
        print('jogada inválida!')

elif computador == 2: #computador jogou tesoura
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('JOGADOR PERDEU')
    else:
        print('jogada inválida!')