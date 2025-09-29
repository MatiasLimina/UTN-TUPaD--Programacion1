#Ahorcado de frutas
import random
def elegir_palabra (palabras): #Selecciona una palabra random para jugar
    num_random = random.randrange(0,len(palabras))
    return palabras[num_random]

def ocultar_palabra(palabra_ocul):
    len_oculta = len(palabra_ocul)
    oculta = ""
    for i in range(len_oculta):
        oculta = oculta + "_"
    return oculta

def array_palabra(palabra):
    aux_palabra = []
    for i in range(len(palabra)):
        aux_palabra.append(palabra[i])
    return aux_palabra

def array_oculta(palabra_oculta):
    aux_oculta = []
    for i in range(len(palabra_oculta)):
        aux_oculta.append(palabra_oculta[i])
    return aux_oculta



def jugar_turno(array_palabra,array_oculta):
    letra = input("Ingrese una letra ").lower()
    acierto = False
    for i in range(len(array_palabra)):
        if array_palabra[i] == letra:
            array_oculta[i] = letra
            acierto = True
    if acierto:
        return array_oculta
    else:
        return False


def mostrar_ahorcado(oculta):
    print(f"{oculta} / Quedan x intentos")

#main
palabras = ["pera", "manzana","banana","naranja"]
palabra_ahorcado = elegir_palabra(palabras)
oculta = ocultar_palabra(palabra_ahorcado)
intentos = 0
print (palabra_ahorcado)
print(oculta)
aux_palabras = array_palabra(palabra_ahorcado)
aux_ocultas = array_oculta(oculta)

salir = False
while not salir:
    turno = jugar_turno(aux_palabras,aux_ocultas)
    if turno == False:
        intentos += 1
    else:
        oculta=turno
        mostrar_ahorcado(oculta)
    if intentos == 6:
        print("Intentos maximos alcanzados \n Perdiste!")
        salir == True
    elif oculta == palabra_ahorcado:
        mostrar_ahorcado(oculta)
        print("Felicitaciones!")
        salir = True

