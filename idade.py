from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
if idade <= 9:
  print('Quem nasceu em {} tem {} anos. Sua categoria é: Mirim'.format(ano, idade))
elif idade <= 14:
  print('Quem nasceu em {} tem {} anos. Sua categoria é: Infantil.'.format(ano, idade))
elif idade <= 19:
  print('Quem nasceu em {} tem {} anos. Sua categoria é: Junior.'.format(ano, idade))
elif idade <= 25: 
  print('Quem nasceu em {} tem {} anos. Sua categoria é Senior.'.format(ano, idade))
elif idade > 25:
  print('Quem nasceu em {} tem {} anos. Sua categoria é: Master.'.format(ano, idade))