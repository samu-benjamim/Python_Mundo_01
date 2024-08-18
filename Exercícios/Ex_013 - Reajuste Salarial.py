salario = float(input("Qual o salário do funcionario? R$"))
aumento = salario + (salario * (15/100))
print("O funcionario que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}".format(salario, aumento))