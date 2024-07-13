creatArray = []
control = True
print("----------------------------------------------------------")
print("Bienvenido al programa para encontrar el promedio de datos")
print("----------------------------------------------------------")
print("Elija una de las siguientes opciones")
print("Escriba 1 para agregar un nuevo número")
print("Escriba 2 para salir y encontrar el promedio")
print("----------------------------------------------------------")

while control == True:
  
  opc = int(input("Desea agregar un nuevo número:  "))
  if opc == 2:
    control = False
    print("Acontinuación se presentará el promedio, espere")
    print("----------------------------------------------------------")
  elif opc != 1 and opc != 2:
    print("Elije una opción valida")
  elif opc == 1:
    creatArray.append(int(input("Ingrese el número entero por favor: ")))
#sumaArray = 0
#for n in range(len(creatArray)):
  #sumaArray = sumaArray + creatArray[n]
#promedioArray = sumaArray/len(creatArray) 
print(creatArray)
print(f"El promedio es: {(sum(creatArray)/len(creatArray))}")