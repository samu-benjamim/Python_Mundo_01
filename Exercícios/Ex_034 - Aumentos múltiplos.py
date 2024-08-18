sal = float(input("Qual é o salário do funcionário? "))
if sal <= 12500:
    sal_novo = sal + (sal * (15/100))
else:
    sal_novo = sal + (sal * (10/100))
print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(sal, sal_novo))    