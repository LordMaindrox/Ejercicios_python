#Ejerccio 1
print("Bienvenidos al programa Resultados de multiplicaciones")
numbersArray = []
x = 0
elementsArray = int(input("Escribe un número entero que serà el numero de elementos que tendra el arreglo: "))
while (x < elementsArray):
  element = int(input("Escriba un numero entero: "))
  numbersArray.append(element)
  x = x + 1
multiplicador = int(input("Escribe un número entero por el que los quieras multiplicar"))
for i in range(elementsArray):
  result = numbersArray[i]*multiplicador
  print(result)
  print(f"{numbersArray[i]} X {multiplicador} = {result}")