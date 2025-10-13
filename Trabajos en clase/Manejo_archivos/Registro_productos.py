import csv
productos = [
    {"nombre":"papa","precio":15},
    {"nombre":"tomate","precio":10}
]
try:
    with open("Productos.csv","w",newline="") as archivo:
        campos = ["nombre","precio"]
        escritor = csv.DictWriter(archivo,fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(productos)
    with open("Productos.csv","r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(fila)
        
except FileExistsError:
    print("El archivo ya existe")

