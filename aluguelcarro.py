km = float(input('Digite quantos km foram percorridos: '))
dias = float(input('Digite quantos dias o carro foi usado: '))
vt = (km*0.15)+(dias*60)
print('o valor a se pagar por {} dias e {} km rodados é R${:.2f}'.format(dias, km, vt))