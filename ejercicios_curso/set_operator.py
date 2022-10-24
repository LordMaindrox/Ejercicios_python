
my_set1 = {1,2,3}
my_set2 = {3,4,5}



#LA UNIÓN
#la unión se hace con el pipe(|) y el resultado es un set que continene los elementos no repetidos de ambos
my_set3 = my_set1|my_set2
print(my_set3)

# LA INTERSECCIóN 
# solo es dejas los elementos que tienen en comun entre ambos conjuntos
#se ocupa el operador ampersan & y como resultado da el elemento que es común entre ambos sets

my_set4 = my_set1 & my_set2
print(my_set4)

# LA DIFERENCIA
#quita los elementos que se encuentren en el otro set con el que se resta por lo que veamos el ejemplo
#caso 1 si restamos el set2 del set1 obtendremos que el set5 queda formado solo por los elementos
#que no estaba en set2, por eso solo se muestra un set con 1 y 2, ya que el 3 estaba en el set2 tambien
#y por eso se quita
my_set5 = my_set1 - my_set2
print(my_set5)
#en este caso, el set6 resulta solo con 4 y 5, porque al restar el set1 el elemento 3 esta presente
#en ambos por lo que se quita del set original dando como resultado soplo el 4 y 5
my_set6 = my_set2 - my_set1
print(my_set6)

#DIFERENCIA SIMÉTRICA

#es lo contrario de la interscción, es el resultado de quedarse con ambos sets
#pero quitando los elementos que son comunes entre ambos 
# usa el operador ^
my_set5 = my_set1 ^ my_set2
print(my_set5)