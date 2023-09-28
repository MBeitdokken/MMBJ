#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:13:11 2023

@author: bjartelandrak
"""

def sum_over_fem(liste): #Vi definerer en funksjon kalt sum_over_fem som tar inn en liste som argument, kalt liste.
    total_sum = 0 #Vi initialiserer en variabel kalt total_sum til 0. Denne variabelen skal holde summen av tallene i lista som er større enn 5.
    for tall in liste: #Vi bruker en for-løkke til å iterere gjennom hvert tall i liste.
        if tall > 5:
            total_sum += (tall - 5)
            #Inne i løkken sjekker vi om det gjeldende tallet tall er større enn 5 ved å bruke betingelsen if tall > 5:.
            #Hvis tallet er større enn 5, trekker vi 5 fra tallet (tall - 5) for å finne differansen mellom tallet og 5, og legger denne differansen til total_sum.
    return total_sum

# Eksempel på bruk:
min_liste = [4, 7, 15]
resultat = sum_over_fem(min_liste)
print(f"Summen av tall over 5 i lista er: {resultat}")