num = input("Informe um número: ")
print("Analisando o número {}.".format(num))
n_num = len(num)
if n_num == 1:
    print("Unidade: {}". format(num[0]))
elif n_num == 2:
    print("Unidade: {}". format(num[1]))
    print("Dezena: {}". format(num[0]))
elif n_num == 3:
    print("Unidade: {}". format(num[2]))
    print("Dezena: {}". format(num[1]))
    print("Centena: {}". format(num[0]))
elif n_num == 4:
    print("Unidade: {}". format(num[3]))
    print("Dezena: {}". format(num[2]))
    print("Centena: {}". format(num[1]))
    print("Milhar: {}". format(num[0]))
else:
    print("Esse programa analisa apenas até o número 9.999.")