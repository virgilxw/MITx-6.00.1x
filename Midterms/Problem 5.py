# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:48:18 2016

@author: Reuben
"""

def dotProduct(listA, listB):
    
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    sum = 0
    
    for i in range(len(listA)):
        sum += listA[i] *listB[i]
        
    return sum