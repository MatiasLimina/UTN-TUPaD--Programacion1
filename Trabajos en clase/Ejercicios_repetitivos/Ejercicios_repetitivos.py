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

#Ejercicio "while"

salir = False
import random
puntaje_jugador = 0
puntaje_maquina = 0
while salir == False:
    jugador = int(input("Eliga una opcion: 1) Piedra \n 2) Papel \n 3) Tijeras "))
    maquina = random.randrange(1,3)
    if jugador == maquina:
        print("Empate")
        puntaje_jugador += 1
        puntaje_maquina += 1
    elif (jugador == 1 and maquina == 2) or (jugador == 2 and maquina == 3) or (jugador ==  3 and maquina == 1):
        print("Gana máquina")
        puntaje_maquina +=1
    else:
        print("Gana jugador")
        puntaje_jugador +=1
    print(f"El puntaje actual es de: jugador {puntaje_jugador} - máquina {puntaje_maquina}")
    sal = input("Desea salir? 1) SI 2) NO ").upper()
    if sal == "SI":
        salir=True

print(f"Puntaje final: jugador {puntaje_jugador} - máquina {puntaje_maquina}")

