#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 23:16:32 2023

@author: bjartelandrak
"""

def longestZeroRain(array: list):
    longest = 0
    current = 0

    for n in array:
        if n == 0:
            current += 1
        else: 
            current = 0
        
        if current > longest:
            longest = current

    return longest


arr1 = dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]

print(longestZeroRain(arr1))