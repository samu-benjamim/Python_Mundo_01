vel = float(input("Qual é a velocidade atual do carro em Km/h? "))
if vel > 80:
    dif = vel - 80
    valor = float(dif * 7)
    print("MULTADO! Você execedu o limite permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R${:.2f}".format(valor))
print("Tenha um bom dia! Dirija com segurança!")