#exercicio 07
#entrada
a = float(input("informe o tamanho do primeiro lado: "))
b = float(input("informe o tamanho do segundo lado: "))
c = float(input("informe o tamanho do terceiro lado: "))

#processo
if (a + b < c) or (a + c < b) or (b + c < a):
    print("não é um triângulo")

elif (a == b) and (a == c):
    print("Este triângulo é Equilatero")

elif (a == b) or (a == c) or (b == c):
    print("Este triângulo é Isóceles")

else:
    print("Este triângulo é Escaleno")