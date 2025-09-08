import random
filas = 5
columnas = 5
carton_bingo1 = [[0 for  _ in range (columnas)]for _ in range(filas)]
numeros = random.sample(range(1,51), 25)
numeros_sorteo = numeros
print (numeros)
for i in carton_bingo1:
    for j in i:
        print(j,end=" ")
    print()

for i in range(filas):
    for j in range(columnas):
        carton_bingo1[i][j] = numeros.pop() 
        print (carton_bingo1[i][j],end =" ")
    print()
print(carton_bingo1)

for x in numeros_sorteo:
    for i in range(filas):
        for j in range(columnas):
            if carton_bingo1[i][j] == x:
                carton_bingo1[i][j] = 0
            else:
                break        


print(carton_bingo1)