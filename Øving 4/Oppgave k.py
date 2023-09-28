#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:15:59 2023

@author: bjartelandrak
"""

def minsteKvadratersMetode(x: list, y: list):
    n = len(x)

    upper = 0
    lower = 0

    xAverage = sum(x) / len(x)
    yAverage = sum(y) / len(y)

    for i in range(n):
        upper += (x[i]-xAverage)*(y[i]-yAverage)
        lower += (x[i]-xAverage)**2

    a = upper / lower
    b = yAverage - a * xAverage

    return (a,b)

from lister_for_del_1 import *

a,b = minsteKvadratersMetode(temperaturer,temperaturer_tidspunkter)

if a > 0:
    print("Trenden på temperaturen er stigende")
elif a < 0:
    print("Trenden på temperaturen er synkende")
else:
    print("Trenden på temperaturen er verken synkende eller stigende")