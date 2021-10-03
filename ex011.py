largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura:2}x{altura:2} e sua área é de {area:2}m2.')
print(f'Para pintar a parede, você precisará de {tinta:} litros de tinta.')