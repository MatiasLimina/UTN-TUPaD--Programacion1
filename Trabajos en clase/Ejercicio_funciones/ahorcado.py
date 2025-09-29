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

def array_palabra(palabra:str,palabra_oculta):
    aux_palabra = []
    aux_oculta= []
    for i in range(len(palabra)):
        aux_palabra.append[palabra[i]]
        aux_oculta.append[palabra_oculta[i]]


def mostrar_ahorcado(oculta):
    print(f"{oculta} / Quedan x intentos")

#main
palabras = ["pera", "manzana","banana","naranja"]
palabra_ahorcado = elegir_palabra(palabras)
oculta = ocultar_palabra(palabra_ahorcado)
intentos = 0
print (palabra_ahorcado)
print(oculta)

salir = False
while not salir:
    turno = intento_letra(palabra_ahorcado,oculta)
    if turno == False:
        intentos += 1
    else:
        oculta=turno
        mostrar_ahorcado(oculta)
    if intentos == 6:
        print("Intentos maximos alcanzados \n Perdiste!")
        salir == True

