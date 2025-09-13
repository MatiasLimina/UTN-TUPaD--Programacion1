
"""
2. Cruce de matrices (tablero naval)

Crear dos matrices 5x5:

Una representa un “océano” con barcos colocados aleatoriamente (con 1 = barco y 0 = agua).

Otra representa los disparos de un jugador.

Cada vez que el jugador dispara, se marca con una “X” si fue acierto o “O” si fue fallo.

El juego termina cuando todos los barcos son hundidos.
👉 Similar al Bingo, pero con coordenadas y validaciones.

"""
import random
lista_datos = [0,1]
MAX_BARCOS = 5
barcos_hundidos_usuario = 0
barcos_hundidos_pc = 0

def crear_barcos(barcos_cont):
    if barcos_cont < 5:
        pos = random.randint(0,1)
        return pos
    else:
        pos = 0
        return pos



matriz_usuario = [[0 for  _ in range (MAX_BARCOS)]for _ in range(MAX_BARCOS)]
matriz_pc = [[0 for  _ in range (MAX_BARCOS)]for _ in range(MAX_BARCOS)]

def imprimir_matriz_u (m_u):
    for i in range (5):
        for j in range(5):
            print(m_u[i][j],end = " ")
        print()
def imprimir_matriz_pc(m_pc):
    for i in range (5):
        for j in range(5):
            print(m_pc[i][j],end = " ")
        print()

for i in range(MAX_BARCOS):
    print(matriz_pc[i])
print("---------------")
for i in range(MAX_BARCOS):
    print(matriz_usuario[i])

imprimir_matriz_pc(matriz_pc)
imprimir_matriz_u(matriz_usuario)
contador = 0
for i in range (5):
        for j in range(5):
            matriz_pc[i][j] = crear_barcos(contador)
            if matriz_pc[i][j] == 1:
                contador+=1
contador = 0
for i in range (5):
        for j in range(5):
            matriz_usuario[i][j] = crear_barcos(contador)
            if matriz_usuario[i][j] == 1:
                contador+=1


for i in range(MAX_BARCOS):
    print(matriz_pc[i])
print("---------------")
for i in range(MAX_BARCOS):
    print(matriz_usuario[i])

turno_usuario = ""
turno_pc = ""
turnos_jugados_pc = []
turnos_jugados_usuario = []
while barcos_hundidos_pc != MAX_BARCOS  and barcos_hundidos_usuario != MAX_BARCOS:
    turno_usuario = input("Ingrese una cordenada: [n,n]")
    turnos_jugados_usuario.append(turno_usuario)
    
    aux_usuario = turno_usuario.split(",")
    aux_usuario = [int(x) for x in aux_usuario]
    print(f"Primer coordenada: {aux_usuario[0]}  Segunda coordenada: {aux_usuario[1]}")
    print(matriz_pc[aux_usuario[0]][aux_usuario[1]])
    if matriz_pc[aux_usuario[0]][aux_usuario[1]] == 0 :
        print ("Fallaste")
    else:
        print("Le diste! Barco hundido")
        matriz_pc[aux_usuario[0]][aux_usuario[1]] = 0
        barcos_hundidos_pc += 1
    
    turno_pc = f"{random.randint(0,4)},{random.randint(0,4)}"
    print(turno_pc,"Turno PC")
    turnos_jugados_pc.append(turno_pc)
    
    aux_pc = turno_pc.split(",")
    aux_pc = [int(x) for x in aux_pc]
    
    if matriz_usuario[aux_pc[0]][aux_pc[1]] == 0 :
        print ("Fallaste")
    else:
        print("Le diste! Barco hundido")
        matriz_usuario[aux_pc[0]][aux_pc[1]] = 0
        barcos_hundidos_usuario += 1
    print("TABLERO DEL USUARIO ACTUALMENTE")
    for i in range(MAX_BARCOS):
        print(matriz_usuario[i])
    print("TABLERO PC ACTUALMENTE")
    for i in range(MAX_BARCOS):
        print(matriz_pc[i])
    #barcos_hundidos_pc = 5

if barcos_hundidos_pc == 5:
    print("El ganador es el usuario")
elif barcos_hundidos_usuario == 5:
    print("El ganador es la PC")




