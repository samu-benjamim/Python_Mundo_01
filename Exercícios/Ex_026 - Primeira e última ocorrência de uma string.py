fra = str(input("Digite uma frase: ")).strip ().lower()
print("A letra A aparece {} vezes na frase,".format(fra.count("a")))
print("A primeira letra A aparece na posição {}".format(fra.find("a")+1))
print("A última letra A aparece na posição {}".format(fra.rfind("a")+1))