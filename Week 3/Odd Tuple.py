# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:40:17 2016

@author: Reuben
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    ''' 
    oddTuple = ()
    for t in range(len(aTup)):
        if t % 2 == 0:
            oddTuple += (aTup[t],)

    return oddTuple