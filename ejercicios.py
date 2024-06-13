#Variables aliatorias 
#Socia un espacio de variables muestral a aleatoria 
#Aleatoria, la suma de las caras al lanzar dos dados= el resultado 
#Cuales son las posibilidades al lanzar 2 dados
#Y = Suma de las caras de lamnzar 2 dados = 36
# s =  { (1,1)(1,2)}

#Esto es una funcion de masa acumulada 
#Investigar, sacar probabilidades integrando 
# Probabilidad que me de 2  p(y=2)= 1/36
#BUCLE ANIDADO 
sumas ={}  #anidar igual se usa[[]]
for i in range(1,7):
    print("\n")
    for j in range(1,7):
    print(i+j, end = "\t")
    if(sumas(i +j, -1) == -1)
      sumas [i+j] = 0
    else:
       sumas[i+j] += 1


sumas

# con una manera m+a sencilla, con un diccionario 
#Sacaremos una matriz que imprima las sumas y luego line 12
sumas ={
    2:1
    3:2

}
# Diccionario
#Se utiliza para riego 
probabilidades ={
for key, value in sumas. items():
   probabilidades[key] =round(vaules/36, 2) * 100
probabilidades

}

plt. bar( x = int(probabilidades.keys()))
#Funcion de masa de probabilidad

