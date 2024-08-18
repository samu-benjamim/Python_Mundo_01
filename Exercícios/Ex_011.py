largura = float(input("Qual a largura da sua parede: "))
altura = float(input("Qual a altura da sua parede: "))
area = largura * altura
tinta = area/2
print("Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m²".format(largura, altura, area))
print("Para pintar essa parede, você precisará de {:.3f} litros de tinta".format(tinta))