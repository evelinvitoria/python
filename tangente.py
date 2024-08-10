import math
an = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('o ângulo de {} tem o SENO de {:.2f} o COSSENO de {:.2f} e a TANGENTE de {:.2f}'.format(an, seno, cosseno, tangente))