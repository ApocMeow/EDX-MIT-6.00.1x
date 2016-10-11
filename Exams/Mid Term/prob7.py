# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:18:40 2016

@author: jhuss

"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Here we set up the variables and starting lists.
    # difference and intersect start empty,intersectkeys will give me a list
    # of the keys that match to be used later
    
    keys_a = set(d1.keys())
    keys_b = set(d2.keys())
    
    intersectkeys = keys_a & keys_b
    difference = {}
    intersect = {}

    #add differences from d1 to new dict
    for key in d1:
        if key not in intersectkeys:
            difference.update({key : d1[key]})
    
    #add differences from d2 to new dict
    for key in d2:
        if key not in intersectkeys:
            difference.update({key : d2[key]}) 
            
    for key in intersectkeys:
        intersect.update({key : f(d1[key], d2[key])})
            
    return (intersect, difference)

