dist = float(input("Qual é a distância da sua viagem? "))
if dist > 200:
    custo = dist * 0.50
    print("Você está prestes a começar uma viagem de {:.1f}Km".format(dist))
else:
    custo = dist * 0.45
    print("Você está prestes a começar uma viagem de {:.1f}Km".format(dist))
print("E o preço da sua passagem será de R${:.2f}".format(custo))                 