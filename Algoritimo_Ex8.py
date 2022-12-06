#exercicio 08
#entrada
ano = int(input("Qual ano deseja pesquisar?"))

#process
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(f'o ano de {ano} é considerado bissexto')

else:
    print(f"o ano de {ano} não é um ano bissexto")