print('=-'*20)
print('emprestimo bancario')
print('=-'*20)
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do seu Salário? '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos*12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestacao))
print('=-'*20)
if prestacao >= minimo:
  print('Emprestimo negado!!!')
else:
  print('Parabêns. Emprestimo aceito!!!')
print('=-'*20)