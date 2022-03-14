'''
55) [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de
agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
tentativas para tentar acertar.
'''

from random import randint
erros = 4
acertos = 0

while erros > 0 and acertos <= 4:

    jogador = int(input('Diga um número de 1 a 10: '))
    computador = randint(1,10)



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