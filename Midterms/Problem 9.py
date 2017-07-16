# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 21:48:18 2016

@author: Reuben
"""
'''
Problem 9
1 point possible (ungraded)
Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
'''
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    tempList = []
    for i in aList[:]:
        if isinstance(i, list):
            x = flatten(i)
            tempList.extend(x)
        else:
            tempList.append(i)
    
    return tempList