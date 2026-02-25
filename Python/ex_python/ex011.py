largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede mede {largura:.3f}x{altura:.3f} sua área é {area:.3f}m².')
print(f'Você gastará {tinta:.3f}L de tintas.')