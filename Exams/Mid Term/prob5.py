# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 12:54:57 2016

@author: jhuss
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    For example, if listA = [1, 2, 3] and listB = [4, 5, 6], 
    the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
    '''
    total = 0
    for n in range(len(listA)):
        total += listA[n] * listB[n]
    print(total)
    
