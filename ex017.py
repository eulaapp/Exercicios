from math import sqrt

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

h = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
h = sqrt(h)

print(f'A hipotenusa vai medir {h:.2f}')

