def run():
    cadena = "Hola mundo Total"
    numero = len(cadena)
    
    for i in range (numero,-1,-1):
        valor = i-1
        if valor >=0:
            caracter = cadena[valor]
            print(caracter)


if __name__ == '__main__':
    run()
