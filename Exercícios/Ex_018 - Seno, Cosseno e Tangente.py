from math import radians, sin, cos, tan
num = float(input("Digite um ângulo: "))
ang = radians(num)
print("O ângulo de {} tem o SENO de {:.2f}.".format(num, sin(ang)))
print("O ângulo de {} tem o COSSENO de {:.2f}.".format(num, cos(ang)))
print("O ângulo de {} tem a TANGENTE de {:.2f}.".format(num, tan(ang)))