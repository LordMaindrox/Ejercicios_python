#Calculadora
from math import prod
control = True
numeros = []
totalSuma = []
totalResta = []
totalMultiplicar = []
totalDividir = []
print("------------------------")
print("Bienvenido a Calculadora")
print("------------------------")
while control == True:
    print("------------------------")
    print("1. Introducir valores")
    print("2. Sumar valores")
    print("3. Restar valores")
    print("4. Multiplicar valores")
    print("5. Determinar pares o impares")
    print("6, Borrar memoria")
    print("7. Salir")
    print("------------------------")
    opc = int(input("Introduce la opción deseada: "))
    if(opc>=1 and opc <=7):
        if opc == 1:
            num = int(input("¿Cuantos números quieres guardar?: "))
            for i in range(num):
                numero = int(input(f"Introduzca el numero {i+1}: "))
                numeros.append(numero)
            print("------------------------")
            print(f"Estos son los numeros que agregaste  {numeros}")
            print("------------------------")
        elif opc == 2:
            num = int(input("¿Cuantos números quieres sumar?: "))
            for i in range(num):
                numeroSuma = float(input(f"Introduzca el numero {i+1}: "))
                totalSuma.append(numeroSuma)
            print("------------------------")
            print(f"Estos son los numeros que agregaste  {totalSuma}")
            print(f"El resultado de la suma es:  {sum(totalSuma)}")
            print("------------------------")
        elif opc == 3:
            num = int(input("¿Cuantos números quieres restar?: "))
            for i in range(num):
                numeroResta = float(input(f"Introduzca el numero {i+1}: "))
                totalResta.append(numeroResta)
            print(f"Estos son los numeros que agregaste  {totalResta}")
            def restar(totalResta):
                if len(totalResta) == 0:
                    return 0
                elif len(totalResta) == 1:
                    return totalResta[0]
                else:
                    return restar(totalResta[:-1]) - totalResta[-1]
            print("------------------------")
            print(f"La respuesta es: {restar(totalResta)}")
            print("------------------------")
        elif opc == 4:
            num = int(input("¿Cuantos números quieres multiplicar?: "))
            for i in range(num):
                numeroMultiplicar = float(input(f"Introduzca el numero {i+1}: "))
                totalMultiplicar.append(numeroMultiplicar)
            print("------------------------")
            print(f"Estos son los numeros que agregaste  {totalMultiplicar}")
            print(f"El resultado de la multiplicación es: {prod(totalMultiplicar)}")
            print("------------------------")
        elif opc == 5:
            evaluar= float(input("Escriba el número a evaluar:  "))
            modulo = evaluar%2
            if modulo == 0:
                print("------------------------")
                print(f"El número {evaluar} es nùmero par")
                print("------------------------")
            else:
                print("------------------------")
                print(f"El nùmero {evaluar} es impar")
                print("------------------------")
        elif opc == 6:
            borrado1 = numeros.clear()
            borrado2 = totalSuma.clear()
            borrado3 = totalResta.clear()
            borrado4 = totalMultiplicar.clear()
            borrado5 = totalDividir.clear()
        elif opc == 7:
            control = False
            print("------------------------")
            print("Gracias por participar, hasta luego")
            print("------------------------")
    else :
        print("////////////////////////")
        print("Elige una opción válida")
        print("////////////////////////")
