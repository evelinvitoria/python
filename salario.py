salario = float(input('Qual é o salario do funcionario? R$ '))
if salario <= 1250:
   novo = salario + (salario * 15 / 100)
   print('Seu novo salário com reajuste é de R${:.2f}'.format(novo))
else:
   new = salario +  (salario * 10 /100)
   print('Seu novo salario com reajuste é de R${:.2f}'.format(new))