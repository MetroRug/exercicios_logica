"""
32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
"""
from random import randint
erros = 5
acertos = 0

while erros > 0 and acertos <= 4:

    jogador = int(input('Diga um número de 1 a 5: '))
    computador = randint(1,5)



    if jogador == computador:
        print('ACERTOU!')
        acertos += 1
        print(f'Você teve {acertos} acertos.')
    elif jogador != computador:
        print(f'Você escolheu {jogador} e o computador escolheu {computador}')
        erros -= 1
        print(f' Você ainda tem {erros} chances.')

if acertos == 5:
    print('Você ganhou!')
elif erros == 0:
    print('Você perdeu!')

