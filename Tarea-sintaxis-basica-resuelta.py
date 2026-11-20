"""
Una estació meteorològica ha registrat les temperatures màximes dels darrers set dies.

Desenvolupa un programa que:
1. Calculi la temperatura mitjana de la setmana.
2. Identifiqui la temperatura màxima i la mínima.
3. Comptabilitzi quants dies s'han superat els 22 °C.
4. Mostri per pantalla cada temperatura i indiqui si és superior o inferior a la mitjana setmanal.
Restricció: No es poden utilitzar llibreries externes.
"""


## Temperatura media de la semana
Temperaturas = [15, 9, 22, 25, 18, 20, 30]
mitjana = sum(Temperaturas)/ len(Temperaturas)

## Máximo temperatura
Temperaturas = [15, 9, 22, 25, 18, 20, 30]

max_temp = max(Temperaturas)
min_temp = min(Temperaturas)
print("La temperatura máxima és:", max_temp)


## Días con más de 22 grados

dias = 0
for temp in Temperaturas:
    if temp > 22:
        dias +=1


## Día de la semana mayor o igual que la media
for dia, temp in enumerate(Temperaturas, start =1):
    if temp > mitjana:
        classificacion = "Superior"
    elif temp < mitjana: 
        classificacion = "Inferior"

    else:
        classificacion = "igual"


# Resumen 

print(f"Temperatura media: {mitjana:.2f} grados")



## CORRECCIÓN ##

"""
Una estació meteorològica ha registrat les temperatures màximes dels darrers set dies.

Desenvolupa un programa que:
1. Calculi la temperatura mitjana de la setmana. (sum, len)
2. Identifiqui la temperatura màxima i la mínima.
3. Comptabilitzi quants dies s'han superat els 22 °C.
4. Mostri per pantalla cada temperatura i indiqui si és superior o inferior a la mitjana setmanal.
Restricció: No es poden utilitzar llibreries externes.
"""
temperatures = [18, 21, 19, 24, 27, 23, 20]

#1. Calculi la temperatura mitjana de la setmana. (sum, len)
mitjana = sum(temperatures) / len(temperatures)

#2. Identifiqui la temperatura màxima i la mínima.
temp_max = max(temperatures)
temp_min = min(temperatures)

#3. Comptabilitzi quants dies s'han superat els 22 °C.
dias = 0
for temp in temperatures:
    if temp > 22:
        dias = dias + 1

#4. Mostri per pantalla cada temperatura i indiqui si és superior o inferior a la mitjana setmanal.
for dia, temp in enumerate(temperatures, start=1):
    if temp > mitjana:
        classificacion = "Superior a la mitjana"
    elif temp < mitjana:
        classificacion = "Inferior a la mitjana"
    else:
        classificacion = "Igual a la mitjana"

    print(f"Dia {dia}: {temp} ºC - {classificacion}" )

#Resumen
print(f"Temperatura mitjana: {mitjana:.2f} ºC")
print(f"Temperatura màxima: {temp_max} ºC")
print(f"Temperatura mínima: {temp_min} ºC")
print(f"Dies amb més de 22ºC: {dias}")
