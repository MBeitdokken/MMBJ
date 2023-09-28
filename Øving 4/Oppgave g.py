#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:56:56 2023

@author: bjartelandrak
"""

def beregn_trend(x, y): #Først definerer vi en funksjon kalt beregn_trend som tar inn to lister som argumenter, x og y. Vi beregner antall datapunkter i listene x og y ved å bruke len(x), som gir oss verdien n. Dette er antallet datapunkter vi har i datasettet.
    n = len(x) #Vi beregner gjennomsnittet av x-verdiene (x̄) ved å summere alle x-verdiene og deretter dele summen på n.
    
    # Beregn gjennomsnittet av x- og y-verdiene
    x_gjennomsnitt = sum(x) / n #Vi beregner gjennomsnittet av x-verdiene (x̄) ved å summere alle x-verdiene og deretter dele summen på n.
    y_gjennomsnitt = sum(y) / n #På samme måte beregner vi gjennomsnittet av y-verdiene (ȳ) ved å summere alle y-verdiene og deretter dele summen på n
    
    # Beregn a (stigningstallet)
    numerator = sum((x[i] - x_gjennomsnitt) * (y[i] - y_gjennomsnitt) for i in range(n))
    denominator = sum((x[i] - x_gjennomsnitt) ** 2 for i in range(n))
    a = numerator / denominator
    
    #Nå beregner vi a (stigningstallet) ved å bruke formelen som tar i bruk gjennomsnittene av x- og y-verdiene. Vi itererer gjennom datapunktene og bruker formlene for teller og nevner i brøken.

    
    # Beregn b (skjæringspunktet)
    b = y_gjennomsnitt - a * x_gjennomsnitt
    #Til slutt beregner vi b (skjæringspunktet) ved å bruke gjennomsnittet av y-verdiene, gjennomsnittet av x-verdiene og stigningstallet a.
    
    return a, b

# Eksempel på bruk:
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

a, b = beregn_trend(x, y)
print(f"Trenden er gitt ved: verdi = {a}x + {b}")
