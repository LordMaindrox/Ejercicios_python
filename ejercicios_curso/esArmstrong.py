import math

def es_armstrong(numero):
    if numero ==0:
        print("No es número Armstrong")
    else:
        sum = 0
        largo = int(math.log10(numero))+1
        for unidad in str(numero):
            valor = (int(unidad)**largo)
            sum = sum+valor
    
    if sum == numero:
        return print("Es número Armstrong")
    return print("No es número Armstrong")

es_armstrong(153)
es_armstrong(1634)
es_armstrong(54748)
es_armstrong(8208)
es_armstrong(9474)
es_armstrong(92727)
