""" Las tuplas, son similares a las listas pero son inmutables, una vez creada una tupla no puedes modificarla,
 ni añadir elementos ni eliminar elementos
 Las tuplas va siempre entre ()"""

coordenadas = (42.83736, 2.83736)
print (coordenadas [0])

lat, lon = coordenadas #para desempaquetar el contenido de una tupla
print(lat)

""" Diccionarios, mantienen el orden en versiones más modernas de Python, de insercción en los diccionarios, 
una clave no la puedes modificar, pueden contener una lista, y para acceder a los elementos del diccionario utilizamos
la clave"""

"""Los conjuntos"""

"""Los Arrays"""

import array
enters = array.array('i'[1,2,3,4])
print(enters)


import numpy as np

""" Numpy nos permite crear vectores o matrices de grandes dimensiones"""

matriu = np.array([[1,2,3],[4,5,6]])
print(matriu.shape)


## Funciones para crear estos tipos de datos con numpy
list()
tuple()
dict()
set()

""" Con estas funciones yo puede tener un tipo de función y convertirlo a otro"""

t = (1,2,3)
l = list(1,2,3)
print(l)

#Listas: en sintaxis.py

#Tuplas: inmutables -> ()
coordenadas = (41.3879, 2.1699)
print(coordenadas[0])

#coordenadas[0] = 40
lat, lon = coordenadas
print(lat)

#DICCIONARIOS: {}
persona = {
    "nom": "Marc",
    "edat": 30,
    "ciutat": "Barcelona"
}

print(persona["nom"])
persona["edat"] = 31
persona["profesio"] = "Informatica"

for clau, valor in persona.items():
    print(f"Recorrem diccionari: {clau} - {valor}")

for clau in persona.keys():
    print(f"Recorrem diccionari: {clau} - {persona[clau]}")

#CONJUNTOS (set): {}
numeros_duplicats = [1, 2, 2, 3, 4, 4, 5]
conjunt_unic = set(numeros_duplicats)
print(conjunt_unic)

grup_a = {"Anna", "Joan", "Maria"}
grup_b = {"Joan", "Pere", "Lluís"}
print(f"Interseccio: {grup_a.intersection(grup_b)}")
grup_a.add("Jordi")
print(f"Add: {grup_a}")
print(f"Union: {grup_a.union(grup_b)}")
print(f"Difference: {grup_a.difference(grup_b)}")
print(f"Difference: {grup_b.difference(grup_a)}")

#ARRAYS
import array
enters = array.array('i', [1,2,3,4])
print(enters)

import numpy as np
matriu = np.array([[1,2,3],[4,5,6]])
print(matriu.shape)
print(matriu)
print(matriu * 2)

#Funciones para crear estos tipos de datos
#list()
#tuple()
#dict()
#set()

t = (1,2,3)
l = list(t)
print(l)

s = "hola"
l2 = list(s)
print(l2)

c = {1,2,3}
l3 = list(c)
print(l3)

l = [1,2,3]
t = tuple(l)
print(t)

l = [1,2,2,3,3]
c= set(l)
print(c)

parejas =[("nom","Anna"), ("edat",25)]
d = dict(parejas)
print(d)

persona = {"nom":"Marc", "edat": 30}
claus = list(persona.keys())
valors = list(persona.values())
items = list(persona.items())

print("claus ", claus)
print("valors ", valors)
print("items ", items)

print(type(persona))
print(isinstance(persona, list))
print(isinstance(persona, dict))
