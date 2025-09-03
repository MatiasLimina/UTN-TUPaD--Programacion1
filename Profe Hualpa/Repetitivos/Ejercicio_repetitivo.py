
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

for l1 in abc:
    print (l1)
    for l2 in abc:
        print (l2)
        for l3 in abc:
            print(l3)
            for n1 in range(0,10):
                print (n1)
                for n2 in range(0,10):
                    print (n2)
                    for n3 in range(0,10):
                        print (n3)

