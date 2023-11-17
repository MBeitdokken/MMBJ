#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 12:03:06 2023

@author: bjarte
"""

import csv
from datetime import datetime, timedelta

# Path to your CSV file
csv_file_path = 'snoedybder_vaer_en_stasjon_dogn.csv'



# Funksjon for å beregne antall dager med skiføre for en vintersesong
def antall_skiføre_dager(dataset):
    skisesonger = {}

    for row in dataset:
        try:
            dato = datetime.strptime(row[2], "%d.%m.%Y")
        except ValueError:
            continue

        if dato.month >= 10:
            start_dato = datetime(dato.year, 10, 1)
            slutt_dato = datetime(dato.year + 1, 6, 1)
        elif dato.month >= 6:
            start_dato = datetime(dato.year, 10, 1)
            slutt_dato = datetime(dato.year + 1, 6, 1)
        else:
            start_dato = datetime(dato.year - 1, 10, 1)
            slutt_dato = datetime(dato.year, 6, 1)

        # Initialiserer dictionary. For hver skisesong starter telling 0
        if start_dato not in skisesonger:
            skisesonger[start_dato] = 0

        # Hvis snømengde verdi er - sett den til 0
        snomengde = 0 if row[3] == '-' else int(row[3])

        if snomengde >= 20 and start_dato <= dato <= slutt_dato:
            skisesonger[start_dato] += 1

    return skisesonger



# Les data fra CSV-filen
dataset = []
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:
        dataset.append(row)

# Hopper over første rad
header = dataset[0]
dataset = dataset[1:]

# Beregn antall dager med skiføre for hver vintersesong
resultat = antall_skiføre_dager(dataset)

# Skriv ut resultatet
for start_dato, antall_dager in resultat.items():
    slutt_dato = start_dato + timedelta(244)
    #print(f"Skisesong fra {start_dato.strftime('%Y-%m-%d')} til {slutt_dato.strftime('%Y-%m-%d')}: {antall_dager} dager med skiføre.")


# Beregn antall dager med skiføre for hver vintersesong
resultat = antall_skiføre_dager(dataset)

# Opprett lister med x- og y-verdier for trenden
x_koordinat = [start_dato.year for start_dato in resultat.keys()]
y_koordinat = list(resultat.values())    
    
def trend_datasett(x,y): 
    # finner gjennomsnitt av listene sum(n) / lengde(n)
    gjennomsnitt_x = sum(x) / len(x) 
    gjennomsnitt_y = sum(y) / len(y) 

    # Beregner a, stigningstallet
    numerator = sum((x[i] - gjennomsnitt_x) * (y[i] - gjennomsnitt_y) for i in range(len(x)))
    denominator = sum((x[i] - gjennomsnitt_x) ** 2 for i in range(len(x)))

    a = numerator / denominator 

    # beregner skjæringspunktet b, ved å ta gjennomsittav y - a * gjennomsnitt av x 
    b = gjennomsnitt_y - a * gjennomsnitt_x

    return a,b 


# Bruk funksjonen for å beregne trenden
a, b = trend_datasett(x_koordinat, y_koordinat)    
    
    
print(f"Trenden for antall dager med skiføre er: verdi = {a:.2f}x + {b:.2f}")
    
    
    
    
    