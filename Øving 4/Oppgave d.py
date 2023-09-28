#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:34:42 2023

@author: bjartelandrak
"""

def tell_storre_enn_verdi(liste, verdi):
    teller = 0
    for element in liste:
        if element >= verdi:
            teller += 1
    return teller

# Eksempel på bruk:
min_liste = [2.5, 3.0, 1.8, 4.2, 5.7, 2.0]
verdi = 3.0
antall_storre_enn_verdi = tell_storre_enn_verdi(min_liste, verdi)
print(f"Antall elementer større enn eller lik {verdi}: {antall_storre_enn_verdi}")