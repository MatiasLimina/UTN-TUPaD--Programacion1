
abc = "abcdefghijklmnopqrstuvwxyz"
patente_valida = False
while patente_valida == False:
    patente = input("Ingrese su patente ").upper()
    print(len(patente))
    if len(patente) == 6:
        letras_patentes = patente[0:2]
        num_patentes =patente[3:5]

        if letras_patentes.isalpha() and num_patentes.isdigit():
            patente_valida = True
    else:
        print("Ingrese una patente válida")
print("Usted ingreso una patente válida")

#Ingresar una patente y sumarle la enesima 

nueva_patente = int(input("Ingrese cuantas patentes mas sumar y buscar en el sistema"))
patente_2 = ""


# Generar nueva patente
contador = 0
for l1 in abc:
    for l2 in abc:
        for l3 in abc:
            for n1 in range(10):
                for n2 in range(10):
                    for n3 in range(10):
                        patente_2 = abc[n1] + abc[n2] + abc[n2] + str(n1) + str(n2) + str(n3)
                        contador += 1
                        if contador == nueva_patente:
                            print(f"La nueva patente es {patente_2.upper()}")
                            break