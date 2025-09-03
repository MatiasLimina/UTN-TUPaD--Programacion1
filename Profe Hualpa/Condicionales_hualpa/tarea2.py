#Sistemas de calificación con promoción
nombre = input("Ingrese su nombre completo").title()
legajo = input("Ingrese su legajo")

nota1 = int(input("Ingrese su primer nota "))
nota2 = int(input("Ingrese su segunda nota "))
nota3 = int(input("Ingrese su tercer nota "))

promedio = (nota1+nota2+nota3)/3

if nota1 < 4 or nota2 < 4 or nota3 < 4:
    print(f"Alumno: {nombre} \n Legajo: {legajo} \n  ")