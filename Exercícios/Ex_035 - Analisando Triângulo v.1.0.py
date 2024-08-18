print("-="*20)
print("Analise de Triângulos")
print("-="*20)
s1 = float(input("Primeiro Seguimento: "))
s2 = float(input("Segundo Seguimento: "))
s3 = float(input("Terceiro Seguimento: "))
list_s = [s1, s2, s3]
list_s.sort()
if list_s [0] + list_s [1] > list_s[2]:
    print("Esses seguimentos podem formar um triângulo")
else:
    print("Esses seguimentos não podem formar um triângulo")