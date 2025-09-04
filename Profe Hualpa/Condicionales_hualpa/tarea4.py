#Categoría de conductores
nombre = input("Ingrese su nombre completo ").title()
edad = int(input("Ingrese su edad "))
exp = float(input ("Ingrese sus años de experiencia manejando "))
categoria = ""
if edad < 18:
    categoria = "No puede conducir"
elif edad >= 18 and exp < 1:
    categoria = "Principiante"
elif edad >= 21 and (exp >= 1 and exp <= 5):
    categoria = "Conductor intermedio"
elif edad >= 30 and exp > 10:
    categoria = "Conductor profesional"
else:
    categoria = "Conductor estándar"

print(f"{nombre} \n {edad} años \n Experiencia de: {exp} años \n Clasificación: {categoria}")