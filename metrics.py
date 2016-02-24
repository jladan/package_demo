"""
A collection of different metrics that work on finite-dimensional collections of numbers
"""

from numpy import array
from math import sqrt

def l1(x_in, y_in):
    x = array(x_in).flatten()
    y = array(y_in).flatten()
    return sum(abs(x-y))

def l2(x_in, y_in):
    x = array(x_in).flatten()
    y = array(y_in).flatten()
    return sqrt(sum((x-y)**2))

def sup(x_in, y_in):
    x = array(x_in).flatten()
    y = array(y_in).flatten()
    return max(abs(x-y))

def hamming(x_in, y_in):
    x = array(x_in).flatten()
    y = array(y_in).flatten()
    # for some reason, `-` is evaluated as component-wise xor
    difference = (abs(x) >=1 ) - (abs(y) >=1 )
    print(difference)
    return sum( difference * 1)
