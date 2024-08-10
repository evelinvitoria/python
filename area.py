largura = float(input('digite a largura da sua parede: '))
altura = float(input('digite a altura da sua parede:'))
area = largura * altura
litro = area / 2
print('com uma área de {:.2f} você precisará de {} litros de tinta'.format(area, litro))