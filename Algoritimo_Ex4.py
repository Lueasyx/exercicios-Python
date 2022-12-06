#exercicio 04
#entrada
nome = print(input("digite seu nome: "))
idade = int(input("digite sua idade: "))

#processo
if idade <= 8:
  print("sua categotia é infantil A")

elif idade < 13:
  print("sua categoria é Infantil B")

elif idade < 18:
  print("sua categoria é Juvenil A")

elif idade < 21:
  print("sua categoria é Juvenil B")

elif idade >= 21:
  print("sua categoria é Sênior")