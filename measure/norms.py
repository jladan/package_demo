"""
A collection of different norms that work on finite-dimensional collections of numbers
"""

from numpy import array
from math import sqrt

def l1(x_in):
    x = array(x_in).flatten()
    return sum(abs(x))

def l2(x_in):
    x = array(x_in).flatten()
    return sqrt(sum(x**2))

def sup(x_in):
    x = array(x_in).flatten()
    return max(abs(x))

def hamming(x_in):
    x = array(x_in).flatten()
    return sum( ( abs(x) >= 1) * 1 )
