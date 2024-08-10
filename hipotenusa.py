from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
h  = hypot(co, ca)
print('o comprimento da hipotenusa é {:.2f}'.format(h))