#exercicio 05  
#entrada
compra = float(input("Digite o valor da compra: "))

#process
if compra >= 500:
  desconto = (compra * 0.25)
  
elif compra >= 200:
  desconto = (compra * 0.20)
  
else:
  desconto = (compra * 0.15)
  
pagar = compra - desconto
print(f'Sua compra foi de R${round(compra, 2)}')
print(f'Seu desconto foi de R${round(desconto,2)}')
print(f'Você pagará R${round(pagar, 2)}')