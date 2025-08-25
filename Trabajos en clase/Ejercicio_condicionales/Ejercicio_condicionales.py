fecha:str = input("Ingrese la fecha: ")
print(fecha)

dia = fecha.split(",")
dia = dia[0]
dia = dia.lower()
print(dia)

DD = fecha.split(",")
DD = DD[1]
DD = (DD)
print(DD)

DD = DD.split("/")
MM = DD[1]
MM = (MM)

DD = (DD[0])
DD = DD.strip()
print (DD,MM)

if dia.isalpha(): 
    print ("Es valido")
else:
    print("Invalido")

if DD.isnumeric():
    print("Es numero")
else:
    print("No es num")

if MM.isnumeric():
    print("Es numero")
else:
    print("No es num")
