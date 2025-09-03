
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
