from random import shuffle
a1 = str(input('Aluno um: '))
a2 = str(input('Aluno dois: '))
a3 = str(input('Aluno três: '))
a4 = str(input('Aluno quatro: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(' a ordem de apresentação é:')
print(lista)