"""
Created on Wed Sep 7 22:25:16 2016

@author: James
"""

import math
# We need to import the math module for use in this function
def polysum(n, s):
    """
    input : n,s - positive integers where 'n' is the number of sides and 's'
    is the length of each side.
    Returns the sum of the perimeter squared and the area.
    """
    perimeter = n * s
    # This variable is the total length of the boundary of the polygon.
    
    area = (0.25 * n * (s ** 2)) / math.tan(math.pi/n)
    # This variable is the total area of the polygon. This iswhy we needed
    # to import the math module!
    
    return round((perimeter ** 2) + area, 4)
    # Here we do our final calculation and return the value, rounding 
    # it to 4 decimal places as required.