#Ahorcado de frutas
import random
def elegir_palabra (palabras): #Selecciona una palabra random para jugar
    num_random = random.randrange(0,len(palabras))
    return palabras[num_random]

def palabra_oculta(palabra_ocul):
    len_oculta = len(palabra_ocul)
    oculta = ""
    for i in range(len_oculta):
        oculta = oculta + "_"
    return oculta



palabras = ["pera", "manzana","banana","naranja"]
palabra_ahorcado = elegir_palabra(palabras)
oculta = palabra_oculta(palabra_ahorcado)
print (palabra_ahorcado)
print(oculta)