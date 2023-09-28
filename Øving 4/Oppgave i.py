#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:15:09 2023

@author: bjartelandrak
"""


temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
def ListeIFTVerdi(a,b):
    resultat = 0
    for i in range(len(a)):
        if a[i] > b:
            resultat += 1
        
    return resultat

print("Antall dager varmere enn 20 grader:", ListeIFTVerdi(temperaturer,20))
print("Antall dager varmere enn 25 grader:", ListeIFTVerdi(temperaturer,25))
print("Antall dager varmere enn 30 grader:", ListeIFTVerdi(temperaturer,30))

