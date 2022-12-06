#exercicio 11
pao = int(input("digite quantos pães foram vendidos: "))
broa = int(input("digite quantas broas foram vendidas: "))

    #process
itensven = pao+broa
valorpao = 0.30
valorbroa = 1.50
total = (pao*valorpao)+(broa*valorbroa)
poupar = total*0.10

print("************ TOTAL DA CONTA************".center(50))
print(f"o total de itens vendidos foi de {itensven}".center(50))
print(f"o valor final arrecadado é de R${round(total, 2)}".center(50))
print(f"o tanto que deve ser poupado é de R${round(poupar, 2)}".center(50))