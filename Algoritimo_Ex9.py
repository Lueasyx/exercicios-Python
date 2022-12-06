    #exercico 09
  #resto ou modo (ou %)
#entrada
angulo = int(input("Informe o Ângulo: "))
voltas = angulo // 360
quadrante = 0

#process
if(angulo > 360):
  angulo = angulo%360

if(angulo <= 90):
  quadrante = 1
elif(angulo <= 180):
  quadrante = 2
elif(angulo <= 270):
  quadrante = 3
else:
  quadrante = 4

print(f"Deu {voltas} volta(s), está no {angulo}° ângulo e no {quadrante}° quadrante")