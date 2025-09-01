abecedario = "abcdefghijklmnñopqrstuvwxyz"
encriptado = int(input("De cuantos lugares desea correr las letras"))


mensajes = 5
for i in range(0,mensajes):
    mensaje_oficial = input(f"Ingrese el mensaje a encriptar para el oficial {i+1}: ")
    print (mensaje_oficial)
    long_mensaje =int(len(mensaje_oficial))
    for j in range(0,long_mensaje):
        print(mensaje_oficial[j:j+1])
        


