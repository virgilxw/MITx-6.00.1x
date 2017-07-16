# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:28:24 2016

@author: Reuben
"""

def polysum (n, s):
    from math import tan, pi
    
    perimeter = n * s
    
    area = (0.25 * n * (s**2)) / (tan(pi/n))
    
    return round(area + perimeter**2, 4)