dia = int(input("Quantos dias o carro ficou alugado: "))
km = float(input("Quanto Km o carro rodou: "))
custo = (dia * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(custo))
