from random import randint
from time import sleep
intens = ('pedra','papel','tesoura')
computador = randint(0, 2)
print('suas opções são: \n [0] pedra \n [1] papel \n [2] tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(2)
print('-=' * 11)
print(f'computador jogou: {intens[computador]}')
print(f'Jogador jogou: {intens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador ==1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')