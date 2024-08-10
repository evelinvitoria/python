distancia = float(input('Qual a distancia da sua viagem em km? '))
vig1 = distancia * 0.50
vig2 = distancia * 0.45
if distancia > 200:
  print('O valor da sua passagem é R${:.2f}'.format(vig2))
else:
  print('O valor da sua passagem é R${:.2f}'.format(vig1))