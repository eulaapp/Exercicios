import math

num = float(input('Digite o ângulo que deseja: '))

cosseno = math.cos(math.radians(num))
seno = math.sin(math.radians(num))
tangente = math.tan(math.radians(num))

print(cosseno, seno, tangente)