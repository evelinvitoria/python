import random
c = random.randint(0,5) #faz o computador "pensar"
print('Tente advinhar qual numero estou pensando de o a 5...')
j = int(input('Em que número eu pensei? ')) #jogador tenta advinhar
if j == c:
  print('Você acertou!!!')
else:
  print('Você errou!!! pensei no {} e não no {}'.format(c, j))