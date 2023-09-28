#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:56:32 2023

@author: bjartelandrak
"""

def lengste_null_sekvens(min_liste):
    maks_lengde = 0  # Variabel for å lagre lengden på den lengste sekvensen
    gjeldende_lengde = 0  # Variabel for å lagre lengden på den gjeldende sekvensen

    for tall in min_liste:
        if tall == 0:
            gjeldende_lengde += 1
            # Oppdaterer maks_lengde hvis den gjeldende sekvensen er lengre
            if gjeldende_lengde > maks_lengde:
                maks_lengde = gjeldende_lengde
        else:
            gjeldende_lengde = 0  # Nullstiller den gjeldende sekvensen hvis vi ikke har en 0

    return maks_lengde

# Eksempel på bruk:
min_liste = [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
resultat = lengste_null_sekvens(min_liste)
print(f"Lengden på den lengste sammenhengende sekvensen av nuller er: {resultat}")
"""
La meg forklare hvordan funksjonen fungerer:

Vi oppretter to variabler, maks_lengde og gjeldende_lengde, som begge starter med verdien 0. maks_lengde skal holde lengden på den lengste sekvensen av nuller vi har funnet så langt, mens gjeldende_lengde skal holde lengden på den gjeldende sekvensen av nuller mens vi itererer gjennom lista.

Vi bruker en for-løkke til å iterere gjennom hvert tall i lista.

Inne i løkken sjekker vi om det gjeldende tallet er lik 0. Hvis det er tilfelle, øker vi gjeldende_lengde med 1 for å representere at vi har funnet en null i sekvensen.

Vi sammenligner også gjeldende_lengde med maks_lengde for å oppdatere maks_lengde hvis den gjeldende sekvensen er lengre enn den tidligere lengste sekvensen.

Hvis tallet ikke er 0, nullstiller vi gjeldende_lengde, siden sekvensen av nuller er brutt.

Til slutt returnerer funksjonen maks_lengde, som representerer lengden på den lengste sammenhengende sekvensen av nuller i lista.

"""


