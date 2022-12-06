#exercicio 10
#entrada
primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))

print(f"a ordem digitada foi: {(primeiro, segundo, terceiro)}")

#process
if(terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

if(segundo < primeiro):
    aux = segundo
    segundo = primeiro
    primeiro = aux

if(terceiro < segundo):
    aux = terceiro
    terceiro = segundo
    segundo = aux

print(f"a ordem crescente ficaria: {(primeiro, segundo, terceiro)}")