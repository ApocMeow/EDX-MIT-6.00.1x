# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:44:09 2016

@author: jhuss
"""

list1 = [1, 2, [6, 7]]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList
    
    Write a function to flatten a list. The list contains other lists, strings, or ints.
    For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] 
    '''
    flat = []
    for i in aList:
        if type(i) == list:
            flat += (flatten(i))
        else:
            flat.append(i)


    return flat
    
print(flatten(list1))