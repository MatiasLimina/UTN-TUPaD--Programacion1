import random
filas = 5
columnas = 5
carton_bingo1 = [[0 for  _ in range (columnas)]for _ in range(filas)]
numeros = random.sample(range(1,51), 25)

print ("Su carton de bingo es: ")

for i in carton_bingo1:
    print(i)
numeros_sorteo = []
bingo = False
fila_completa= []
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
    #if fila_completa <= 5:
    for indice, fila in enumerate(carton_bingo1):
        if all(x == 0 for x in fila) and indice not in fila_completa:
            fila_completa.append(indice)
            print(f"Linea completa en la fila {indice+1}", carton_bingo1[indice])

    
    
    bingo = all(
        carton_bingo1[i][j] == 0
        for i in range(filas)
        for j in range(columnas)
    )
    if bingo:
        print("¡Bingo!")
        break




print("Su carton completo: ")
for i in carton_bingo1:
    print(i)