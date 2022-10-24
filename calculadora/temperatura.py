def celsiusAKelvin (dato):
    return dato+273.15

def kelvinACelsius (dato):
    return dato-273.15

def celsiusAFahrenheit (dato):
    return (dato * 9/5)+32

def fahrenheitACelcius (dato):
    return (dato -32)* 5/9

def fahrenheitAKelvin (dato):
    return (dato -32)* 5/9+273.15

def kelvinAFahrenheit (dato):
    return ((dato-273.15)* 9/5)+32

control = True

print(kelvinAFahrenheit(30))
print(fahrenheitAKelvin(56))
print("Bienvenidos al programa de conversor de escalas de temperatura")

while control == True :
    print("_______________________________________________________________")
    print("Elige la conversión a realizar")
    print("1.- de grados Celsius a Kelivin")
    print("2.- de grados Kelvin a Celsius")
    print("3.- de grados Celsius a Fahrenheit")
    print("4.- de grados Fahreinheit a Celsius")
    print("5.- de grados Fahreinheit a Kelvin")
    print("6.- de grados Kelvin a Fahrenheit")
    opcp = print(int(input("Qué conversión vas a realizar")))
    if opcp == 1:
        valor = float(input("cifra a evaluar: "))
        print(f'{valor} grados Celsius son {celsiusAKelvin(valor)} grados Kelvin')
    elif opcp == 2:
        valor = float(input("cifra a evaluar: "))
        print(f'{valor} grados Celsius son {kelvinACelsius(valor)} grados Kelvin')