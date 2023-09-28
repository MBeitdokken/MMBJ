#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:50:09 2023

@author: bjartelandrak
"""

def beregn_differanser(liste): #Først definerer vi en funksjon ved navn beregn_differanser som tar inn en liste som argument
    differanser = [] #Innenfor funksjonen oppretter vi en tom liste kalt differanser som vi vil bruke til å lagre differansene mellom tallene i den opprinnelige lista
    for i in range(len(liste) - 1): #Vi bruker en for-løkke til å iterere gjennom elementene i liste fra starten (indeks 0) til nest siste element (indeks len(liste) - 1). Dette er fordi vi skal sammenligne hvert tall med det neste tallet i lista.
        differanse = liste[i+1] - liste[i] #Inne i løkken beregner vi differansen mellom det gjeldende tallet liste[i+1] og det neste tallet liste[i] ved å trekke dem fra hverandre.
        differanser.append(differanse) #Deretter legger vi denne differansen til i den differanser-listen som vi opprettet tidligere.
    return differanser # Til slutt returnerer funksjonen den ferdige listen differanser som inneholder alle differansene mellom tallene i den opprinnelige lista.

# Eksempel på bruk:
min_liste = [3, 7, 1, 9, 4]
differanser = beregn_differanser(min_liste)
print("Differansene mellom hvert tall og neste tall i lista er:", differanser)