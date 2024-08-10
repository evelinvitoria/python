real = float(input('Quanto dinheiro você tem na carteira? R$:'))
dollar = real / 5.25
won = real / 0.0038
print('com R${:.2f} você pode comprar U${:.2f} e KW{:.2f}'.format(real, dollar, won))