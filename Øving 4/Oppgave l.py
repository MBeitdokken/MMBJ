#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:16:16 2023

@author: bjartelandrak
"""

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]

def VoksendePlante(a):
    sum = 0
    for i in range(len(a)):
        if a[i] > 5:
            sum += a[i]-5
    return sum

print("Total vekst: ",VoksendePlante(temperaturer))