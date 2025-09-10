lista_alumnos = [
    "Lautaro Agustín Aguero",
    "Mateo Alejo Algañaraz",
    "Yoselie Aquino",
    "Santiago Facundo Barretto",
    "Ayrton Calderon",
    "María Belén Calvo García",
    "Nicolas Exequiel Carchano",
    "Sergio Joaquin Chiarello Ghilardi",
    "Santino Cárdenas Valls",
    "Octavio Agustin Fiore Montivero",
    "Bruno Fiouchetta",
    "Braian Leandro Flores Marin",
    "Agustina Luz Fontagnol",
    "Maximo Mateo Franco",
    "Facundo Adrian Gomez Romero",
    "Marcelo Hernán Gonzalez",
    "Genaro Guillot",
    "Camilo Javier Illanes Donoso",
    "Matias Nicolas Limina Nuñez",
    "Federico Alejandro Lopez",
    "Jeremías Daniel Luzuriaga",
    "Santino Mantineo",
    "Ezequiel Menéndez",
    "Nicolás Monjelardi",
    "Joel Nicolas Moreno",
    "Nicolás Uriel Moron Gutierrez",
    "Joaquín Morán",
    "Santino Naldini Sosa",
    "Andres Victor Novello",
    "Joseph Oliveros",
    "Santiago Javier Ontivero Parlade",
    "Roberto Paul Paiva",
    "Matías Pereyra",
    "Gianella Sol Peña",
    "Leonel Lautaro Ponce De Leon Martinez",
    "Cristian Nestor Rodriguez Martinez",
    "Ignacio Martín Rodríguez",
    "Rafael Ignacio Ruiz Guiñazú Puebla",
    "Florencia Santos",
    "Marcelo Scherer Huf",
    "Martina Guadalupe Suarez",
    "Elias Emanuel Tello",
    "Agustina Luz Fontagnol"
]
matriz_grupos = []
grupos = len(lista_alumnos)//4
"""
for i in range (0,grupos):
    matriz_grupos.append([])
    print(matriz_grupos[i])
"""
import random
largo_lista = len(lista_alumnos)
lista_nueva_alumn = [[0 for  _ in range (largo_lista)]]
index = random.sample(range(0,largo_lista),largo_lista)


for i in index:
    lista_nueva_alumn.append(lista_alumnos[i])

for i in range(0,largo_lista):
    print(lista_nueva_alumn[i])

