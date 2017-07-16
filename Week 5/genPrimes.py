# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 19:55:27 2016

@author: Reuben
"""

def genPrimes():
    n = 1
    primesList = []
    
    while True:
        n += 1
        for e in primesList:
            if n % e == 0:
                break
        else:
            primesList.append(n)
            yield n
            
