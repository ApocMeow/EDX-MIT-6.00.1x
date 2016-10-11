# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:30:39 2016

@author: jhuss
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    
    closest_power(3,12) returns 2
    closest_power(4,12) returns 2
    closest_power(4,1) returns 0
    '''

    exp = 0.2
    eps = 0.1
    total = base ** exp
    while (total - eps) <= num:
        if total < num:
            exp += 0.2
            total = base ** exp
        else:
            exp -= 0.2
            total = base ** exp
    
    return int(exp)
    

print(closest_power(4, 1))