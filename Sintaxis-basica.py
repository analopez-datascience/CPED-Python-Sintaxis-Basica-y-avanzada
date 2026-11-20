## Sintaxis básica de Python

##  definimos variables con tipor básicos
edad = 25
altura = 1.75
nom = 'ana'
es_estudiante = True

## cuando quiero definir una variable que es constante, lo ponemos en mayúsculas. Es una convencion, las constantes se definen en mayúsculas.
CONTANT = "constante"

## asignaciones multiples 
a, b, c = 1, 2, "Hola"

print("Variables nom: ", nom)

print(f"Variable nom: {nom}")

## funciones relacionadas con cadenas de texto

text = "documente_de_prova.pdf"
print(text.startswith("document"))
print(text.endswith(".pdf"))
print(text.endswith(".jpg"))

posicio = text.find("de")
print(posicio)

# te pone la primera letra en mayúscula
nombre = "maria"
print(nombre.capitalize())

## el comando isdigit nos va permitir saber si algo es un digito devuelve true o flase


paraula = "Python"
texto_amb_espais = "hola mundo"
texto_sense_espais = "codi123"

print(paraula.isalpha())
print(texto_amb_espais.isalpha())
print(texto_sense_espais.isalpha())

## condicionales 
nota = 7
if nota >= 9:
    print("excelente")
elif nota >= 5:
    print("aprobado")
else:
    print("suspenso")

# bucles clásicos

for i in range (3):
        print(i)

# bucle WHILE, se permanece en el bucle mientra se cumpla una condición

##while contador > 5
    ##print(contador)
    ##contador += 1 #amplicar que no estar terminado
    ##pass
# Definición de funciones, pass es una función que no hace nada, pero sirve para que el bloque de codigo no se quede sin implimentar y python no nos de error
## el return si que es obligatorio
def sumar(a,b):
     pass 


def restar (a, b):
     return a-b


def descriure_persona (nom, edat, ciutat):
     return f"Mellamo {nom}, tengo {edat} años y soy de {ciutat}"

print(descriure_persona("ana", 25, "Barcelona"))


## Funciones lambda, son funciones anonimas, no tienen nombre, se usan para cosas muy concretas y no se van a reutilizar. 
## Se usan mucho en programación funcional. Son funciones sin nombre.

quebrado = lambda x: x % 2 != 0


## Importar librerias 
import math
radi = 5
area = math.pi * radi ** 2
print (f"El area del circulo es: {area}")

from datetime import date
avui = date.today()
print(f"Hoy es: {avui}")


## tipos de datos complejos
## Listas, para definir las listas se utiliza el corchete

lista = [1, 2, 3, 4, 5]
fruites = ["manzana", "platano", "pera"]