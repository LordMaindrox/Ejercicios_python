numero = 23519
lista_residuo = []

while numero >0:
        dividir = numero//2
        #print(dividir)
        residuo = numero % 2
        #print(residuo)
        lista_residuo.append(residuo)
        
        numero = dividir
        
#print(lista_residuo)
longitud = len(lista_residuo)

for i in range(longitud-1,-1,-1):
   print(lista_residuo[i], end="")     
