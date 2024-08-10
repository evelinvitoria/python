import random
a1 = str(input('nome do aluno 1: '))
a2 = str(input('o nome do aluno 2: '))
a3 = str(input('o nome do aluno 3: '))
a4 = str(input('o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)
print('o aluno sorteado foi: {}'.format(sorteado))