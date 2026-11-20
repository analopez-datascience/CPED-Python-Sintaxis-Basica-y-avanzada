"""
Una empresa disposa de les vendes mensuals de diferents productes:
vendes = {"Portatils": [1200, 1500, 1100, 1800], "Monitors": [500, 650, 700, 600], 
"Teclats": [100, 150, 120, 180], "Ratolins": [80, 90, 110, 100]}

Cada llista representa les vendes dels quatre primers mesos de l'any, expressades en euros.

Desenvolupa un programa que:
1. Calculi les vendes totals de cada producte i les emmagatzemi en un nou diccionari.
2. Identifiqui el producte amb més vendes acumulades.
3. Calculi la mitjana mensual de vendes per producte.
4. Classifiqui els productes segons les vendes acumulades:
   - Alt: més de 4.000 €.
   - Mitjà: entre 2.000 € i 4.000 €, ambdós inclosos.
   - Baix: menys de 2.000 €.
5. Generi un diccionari amb la classificació dels productes.
6. Identifiqui quin mes ha tingut més vendes totals, considerant tots els productes.
Repte addicional: Ordena els productes de major a menor volum de vendes sense modificar el diccionari original.
"""
vendes = {
    "Portatils": [1200, 1500, 1100, 1800], 
    "Monitors": [500, 650, 700, 600], 
    "Teclats": [100, 150, 120, 180], 
    "Ratolins": [80, 90, 110, 100]
}

#1. Calculi les vendes totals de cada producte i les emmagatzemi en un nou diccionari.
totals = {}
for producte, vendes_mensuals in vendes.items():
    totals[producte] = sum(vendes_mensuals)

#2. Identifiqui el producte amb més vendes acumulades.
producte_maxim = max(totals, key=totals.get)

#3. Calculi la mitjana mensual de vendes per producte.
mitjanes = {}
for producte, vendes_mensuals in vendes.items():
    mitjanes[producte] = sum(vendes_mensuals)/len(vendes_mensuals)

#4. Classifiqui els productes segons les vendes acumulades:
#5. Generi un diccionari amb la classificació dels productes.
classificacions = {}
for producte, total in totals.items():
    if total > 4000:
        categoria = "Alta"
    elif total >= 2000:
        categoria = "Mitja"
    else:
        categoria = "Baix"

    classificacions[producte] = categoria
    
#6. Identifiqui quin mes ha tingut més vendes totals, considerant tots els productes.
totals_mensuals = [0, 0, 0, 0]

for producte, vendes_mensuals in vendes.items():
    for i, import_venda in enumerate(vendes_mensuals):
        totals_mensuals[i] += import_venda
        #totals_mensuals[i] = totals_mensuals[i] + import_venda

mes_maxim1 = totals_mensuals.index(max(totals_mensuals)) + 1

#RESUMEN
for producte in vendes:
    print(f"\nProducte: {producte}")
    print(f"Total: {totals[producte]:.2f} €")
    print(f"Mitjana mensual: {mitjanes[producte]:.2f} €")
    print(f"Classificació: {classificacions[producte]}")

print(f"Producte amb més vendes: {producte_maxim}")
print(f"Mes amb més vendes: {mes_maxim1}")

