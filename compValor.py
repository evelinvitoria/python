a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a 
if b < a and b <c :
  menor = b
if c < a and c < b:
  menor = c
maior = a
if b > a and b > c:
  maior = b
  if c > a and c > b:
    maior = c
print('o maior valor digitado foi {}'.format(maior))
print('o menor valor digitado foi {}'.format(menor))