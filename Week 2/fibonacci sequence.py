# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:22:19 2016

@author: Reuben
"""

def fibonacciRecursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursion(n-2) + fibonacciRecursion(n-1)
        
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)