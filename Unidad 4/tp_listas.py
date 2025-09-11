#Ejercicio 1
lista_mult_4 = list(range(0,101,4))
for i in range(len(lista_mult_4)):
    print(lista_mult_4[i])

#Ejercicio 2
lista_ejer_2=[1,2,3,4,5]
print (lista_ejer_2[-2])

#Ejercicio 3
lista_vacia = []
lista_vacia.append("barco")
lista_vacia.append("avion")
lista_vacia.append("moto")
print(lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Ejercicio 5
"""
El programa saca del arreglo el número mas alto
"""

#Ejercicio 6
lista_30 = list(range(10,31,5))
print("Posicion 1:",lista_30[0],"Posicion 2:",lista_30[1])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Velero"
autos[2] = "Yamaha"
print(autos)

#Ejercicio 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)