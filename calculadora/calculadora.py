#Calculadora
from math import prod


control = True
numeros = []
totalSuma = []
totalResta = []
totalMultiplicar = []
totalDividir = []
while control == True:
    print("------------------------")
    print("Bienvenido a Calculadora")
    print("------------------------")
    print("1. Introducir valores")
    print("2. Sumar valores")
    print("3. Restar valores")
    print("4. Multiplicar valores")
    print("5. Determinar pares o impares")
    print("6. Salir")
    opc = int(input("Introduce la opción deseada: "))
    if(opc>=1 and opc <=6):
        if opc == 1:
            num = int(input("¿Cuantos números quieres guardar?: "))
            for i in range(num):
                numero = int(input(f"Introduzca el numero {i+1}: "))
                numeros.append(numero)
            print(f"Estos son los numeros que agregaste  {numeros}")

        elif opc == 2:
            num = int(input("¿Cuantos números quieres sumar?: "))
            for i in range(num):
                numeroSuma = float(input(f"Introduzca el numero {i+1}: "))
                totalSuma.append(numeroSuma)
            print(f"Estos son los numeros que agregaste  {totalSuma}")
            print(sum(totalSuma))

        elif opc == 3:
            num = int(input("¿Cuantos números quieres restar?: "))
            for i in range(num):
                numeroResta = float(input(f"Introduzca el numero {i+1}: "))
                totalResta.append(numeroResta)
            print(f"Estos son los numeros que agregaste  {totalResta}")
            #a = 1
            for a in range(len(totalResta)):
                resta = totalResta[a]-totalResta[a+1]
                print(resta)

        elif opc == 4:
            num = int(input("¿Cuantos números quieres multiplicar?: "))
            for i in range(num):
                numeroMultiplicar = float(input(f"Introduzca el numero {i+1}: "))
                totalMultiplicar.append(numeroMultiplicar)
            print(f"Estos son los numeros que agregaste  {totalMultiplicar}")
            print(prod(totalMultiplicar))
            
        elif opc == 5:
            evaluar= float(input("Escriba el número a evaluar:  "))
            modulo = evaluar%2
            if modulo == 0:
                print("Es nùmero par")
            else:
                print("Es impar")

        elif opc == 6:
            control = False
            print("Gracias por participar, hasta luego")
    else :
        print("Elige una opción válida")
