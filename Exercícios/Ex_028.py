from random import randint
from time import sleep
print("\033[33m-=-\033[m"*40)
print("\033[34mVou pensar em um número entre 0 a 5. Tente adivinhar....\033[m")
print("\033[33m-=-\033[m"*40)
num = int(input("Em que número eu pensei? \n\033[32m"))
print("\033[35mPROCESSANDO...\033[m")
sleep(2)
escolha = randint(0, 5)
if escolha == num:
    print("\033[32mPARABÉNS! Você conseguiu me vencer!\033[m")
else:
    print("{}GANHEI! Eu pensei no número {} e não no {}!{}".format("\033[31m", escolha, num, "\033[m"))