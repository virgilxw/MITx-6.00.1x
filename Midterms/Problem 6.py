# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:48:18 2016

@author: Reuben
"""

def deep_reverse(L):
    """ 
    assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    
    L.reverse()
    
    for i in range(len(L)):
        L[i].reverse()