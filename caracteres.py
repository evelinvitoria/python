nome=str(input('Digite seu nome: ')).strip()
print('A quantidade de caracteres em seu nome é {}'.format(len(nome) - nome.count(' ')))
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu primeiro nome tem {} caracteres'.format(nome.find(' ')))