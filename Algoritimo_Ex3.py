#exercicio 3
#entrada
alt = float (input(" insira sua altura: "))
sex = input(" digite 1 caso seja homem ou 2 caso for mulher ")

#processo
if sex == 1:
    idealh = (72.7 * alt) - 58
    print(f"seu peso ideal é {round(idealh, 2)}")

else :
    idealm = (62.1 * alt) - 44.7
    print(f"seu peso ideal é {round(idealm, 2)}")