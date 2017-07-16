# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:48:18 2016

@author: Reuben
"""
from math import log

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    
    x = log(num) / log(base)
    diff1 = abs(base ** int(x) - num)
    diff2 = abs(base ** (int(x)+1) - num)
    
    if diff1 == diff2:
        return int(x)
    elif diff1 < diff2:
        return int(x)
    elif diff1 > diff2:
        return int(x)+1