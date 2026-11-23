""" Lectura de archivos de texto y métodos asociados"""
"""
stream = open("./datafiles/feedback_students.txt", "r") # la r por defecto es el modo de lectura, el open text ya lo incluiria
print(stream.read())


stream = open("./datafiles/feedback_students.txt", "rt", encoding="utf-8") 
print(stream.read())
stream.close()

#----------------------#
## con with
"""
## lee todo el archivo y lo devuelve en una lista, si no le especificas lineas las lee todas
"""with open("./datafiles/feedback_students.txt", "rt", encoding="utf-8") as file: ## te crea un contexto relacionado con el archivo y no es necesario hac er el close
    lines = file.readlines() ## lee todas las lineas y las devuelve en una lista, si no le especificas lineas las lee todas
    for line in lines: 
        print(line.strip())"""
"""
## Aquí estamos leyendo linea a linea
with open("./datafiles/feedback_students.txt", "rt", encoding="utf-8") as file:
    for line in file: # devuelve una lista de string, cada posición de mi lista es una línea del archivo.
        print(line.strip()) # strip elimina los espacios en blanco al inicio y al final de la línea
"""
#----------------------#
    """ hay una versión que es más eficienter cuando se lee grandes volumenes de datos, que es leer línea por línea,
      en lugar de leer todo el archivo y luego iterar sobre la lista de líneas
    """

"""with open("./datafiles/feedback_students.txt", "rt", encoding="utf-8") as file:
    line = file.readline() # lee una línea del archivo
    while line != "": # mientras no sea una línea vacía
        print(line.strip())
        line = file.readline() # lee la siguiente línea Hasta que no haya más líneas, readline devuelve una cadena vacía y salimos del bucle
"""
#----------------------#

"""with open("./datafiles/sales_data.csv", "rt", encoding="utf-8") as file:
    for line in file:
        datos = line.strip().split(",") 
        print(datos)
"""
#----------------------#
"""import os
if os.path.exists("./datafiles/sales_data.csv"):
    print ("El archivo existe")
else:
    print ("El archivo no existe")"""

#----------------------#

""" Método de control de excepciones para la lectura de archivos"""
file_path_example ="./datafiles/sales_data.csv"

try:
    with open("./datafiles/sales_data.csv", "rt", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"File '{os.path.basename(file_path_example)}' loaded successfully.")
        for i, line in enumerate(lines):
            print(f"Line {i}, {line.strip()}")
except FileNotFoundError:
    print(f"File not found.")

#----------------------#