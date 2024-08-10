vel = float(input('Qual a velocidade? ')) 
if vel > 80:
  print('Você foi multado!')
  multa = (vel - 80) * 7
  print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
  print('tenha um bom dia. Dirija com segurança!')