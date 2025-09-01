#Ejercicio "for"
abecedario = "abcdefghijklmnñopqrstuvwxyz"
encriptado = int(input("De cuantos lugares desea correr las letras"))


mensajes = 5
for i in range(0,mensajes):
    mensaje_oficial = input(f"Ingrese el mensaje a encriptar para el oficial {i+1}: ").lower()
    mensaje_encrip = ""
    for l in mensaje_oficial:
        if l in abecedario:
            posicion = abecedario.index(l)
            nueva_letra  = abecedario[(posicion+encriptado)%27]
            mensaje_encrip += nueva_letra
        else:
            mensaje_encrip += l
    print(mensaje_encrip)




