def poligono(base,altura,tipo):
    if tipo == 3:
        print((base*altura)/2)
    else: print(base*altura)

def inicio():
    print("""
    Bienvenidos
          Seleccione el tipo de figura para calcular el área
          1.- Cuadrado
          2.- Rectángulo
          3.- Triángulo
    """)
    

def run():
    inicio()
    tipo = int(input("Elija el número del tipo de figura: "))
    base = int(input("Escriba el valor de la base: "))
    altura = int(input("Escriba el valor de la altura: "))
    print("El valor del área de la figura es: ")
    poligono(base,altura,tipo)



if __name__ =='__main__':
    run()