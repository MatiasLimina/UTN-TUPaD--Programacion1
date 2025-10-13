#RUTA_ARCHIVO = "Profe Hualpa\Manejo_de_archivos\listaAlumnosC3.txt"
#RUTA_ARCHIVO = r"C:\AAAUniversidad\Programacion1\UTN-TUPaD--Programacion1\Profe Hualpa\Manejo_de_archivos\listaAlumnosC3.txt"
#Metodo a usar(doble backlash para que python lo interprete como corresponde y lea el archivo correctamente):
RUTA_ARCHIVO ="C:\\AAAUniversidad\\Programacion1\\UTN-TUPaD--Programacion1\\Profe Hualpa\\Manejo_de_archivos\\listaAlumnosC3.txt"
try:
    archivo = open(RUTA_ARCHIVO,"r",encoding="utf-8")

    print ("Contenido del archivo: \n")

    for linea in archivo:
        nombre = linea.strip()
        print(nombre)

except FileNotFoundError:
    print(f"Error: no se encontro el archivo {RUTA_ARCHIVO}")
except PermissionError:
    print(f"Error: no tenes permiso para leer este archivo ")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")
finally:
    try:
        archivo.close()
    except:
        pass