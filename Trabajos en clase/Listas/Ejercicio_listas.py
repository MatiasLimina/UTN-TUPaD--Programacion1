import random
filas = 5
columnas = 5
carton_bingo1 = [[0 for  _ in range (columnas)]for _ in range(filas)]
numeros = random.sample(range(1,51), 25)
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
print("----------------------")

for i in carton_bingo1:
    print(i)
numeros_sorteo = []
bingo = False
while not bingo :
    numero_sorteado = random.randint(1,50)
    if numero_sorteado not in numeros_sorteo:
        numeros_sorteo.append(numero_sorteado)
        print(f"Se sortea el {numero_sorteado}")
    for i in range(filas):
        for j in range(columnas):
            if carton_bingo1[i][j] == numero_sorteado:
                carton_bingo1[i][j] = 0
                print ("Lo tenés")
                break
    
    bingo = all(
        carton_bingo1[i][j] == 0
        for i in range(filas)
        for j in range(columnas)
    )
    if bingo:
        print("¡Bingo!")
        break




print("Nuevo: ",carton_bingo1)