  #exercicio 06
#entrada
nome = input("digite seu nome: ")
peso = float(input("insira o seu peso: "))
alt = float(input("insira sua altura: "))
imc = peso / (alt * alt) 

print(f"seu IMC é {imc}")

#process
if imc < 18:
    print(f"{nome} Você esta abaixo do peso ideal")
elif imc > 18 and imc <= 24: 
    print(f"{nome} Você esta no peso ideal")
elif imc > 25 and imc <= 30:
    print(f"{nome} você está acima do peso ideal")
else:
    print(f'{nome} você está obeso(a)')