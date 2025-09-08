#Sistemas de calificación con promoción
nombre = input("Ingrese su nombre completo").title()
legajo = input("Ingrese su legajo")

nota1 = int(input("Ingrese su primer nota "))
nota2 = int(input("Ingrese su segunda nota "))
nota3 = int(input("Ingrese su tercer nota "))

promedio = (nota1+nota2+nota3)/3

if nota1 < 4 or nota2 < 4 or nota3 < 4:
    print(f"Alumno: {nombre} \n Legajo: {legajo} \n DESAPROBADO DIRECTO ")
elif promedio<6 :
    print(f"Alumno: {nombre} \n Legajo: {legajo} \n Promedio: {promedio} \n DESAPROBADO ")
elif promedio>=6 and promedio<=7:
    print(f"Alumno: {nombre} \n Legajo: {legajo} \n Promedio: {promedio} \n APROBADO CON FINAL ")
else:
    print(f"Alumno: {nombre} \n Legajo: {legajo} \n Promedio: {promedio} \n PROMOCIONADO ")

#Trate de usar colorama para meterle color a lo que muestra en la terminal pero no logre hacerlo andar dsp de 25 min tratando de arreglarlo, dice q no encuentra el modulo