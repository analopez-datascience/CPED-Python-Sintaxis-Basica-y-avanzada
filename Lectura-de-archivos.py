""" Lectura de archivos de texto y métodos asociados"""

stream = open("./datafiles/feedback_students.txt", "r") # la r por defecto es el modo de lectura, el open text ya lo incluiria
print(stream.read())


stream = open("./datafiles/feedback_students.txt", "rt", encoding="utf-8") 
print(stream.read())
stream.close()


## con with
with open("./datafiles/feedback_students.txt", "rt", encoding="utf-8") as file: ## te crea unc ontexto relacionado con el archivo y no es necesario hac er el close
    lines = file.readlines() ## lee todas las lineas y las devuelve en una lista, si no le especificas lineas las lee todas

    for line in lines: # devuelve una lista de string, cada posición de mi lista es una línea del archivo.
        print(line) # strip elimina los espacios en blanco al inicio y al final de la línea