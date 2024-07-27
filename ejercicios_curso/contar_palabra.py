
cadena = "hola mundo hola mundo mundo JESSICA"
contar = 0

recuento = []
diccionario = {}
for palabra in cadena.split():
    #contar = contar +1
    recuento.append(palabra)
    #print(palabra)
#print(contar)
#print(recuento)
for i in recuento:
    marca = 0
    for j in recuento:
        if i ==j:
            marca = marca+1
        diccionario[i] = marca
print(diccionario)

