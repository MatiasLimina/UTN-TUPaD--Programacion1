
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

matriz_usuario = [["-" for  _ in range (MAX_BARCOS)]for _ in range(MAX_BARCOS)]
matriz_pc = [["-" for  _ in range (MAX_BARCOS)]for _ in range(MAX_BARCOS)]

def imprimir_matriz_u (m_u):
    for i in range (MAX_BARCOS):
        for j in range(MAX_BARCOS):
            print(m_u[i][j],end = " ")
    print()
def imprimir_matriz_pc(m_pc):
    for i in range (MAX_BARCOS):
        for j in range(MAX_BARCOS):
            print(m_u[i][j],end = " ")
    print()


for i in range (MAX_BARCOS):
    for j in range(MAX_BARCOS):
        matriz_pc.insert((i,j),random.randrange(0,1))
        imprimir_matriz_pc(matriz_pc)







#while MAX_BARCOS != barcos_hundidos_pc or MAX_BARCOS != barcos_hundidos_usuario:
    


