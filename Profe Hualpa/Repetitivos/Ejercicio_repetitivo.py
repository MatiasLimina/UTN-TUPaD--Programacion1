
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

#Funciones para mover letras y numeros
def move_alphabet(start_letter, steps):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    start_index = alphabet.index(start_letter.upper())
    new_index = (start_index + steps) % len(alphabet)
    return alphabet[new_index]

def move_number(start_number, steps):
    start_number = int(start_number)
    new_number = (start_number + steps) % 10
    return str(new_number)

# Generar nueva patente
