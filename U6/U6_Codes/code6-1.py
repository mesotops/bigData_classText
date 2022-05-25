# -*- coding: utf-8 -*-   [   Code 6-1 :   Similarity Measures   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import math
from decimal import Decimal

def euclidean_distance(x,y):
     return math.sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def manhattan_distance(x,y):
     return sum(abs(a-b) for a,b in zip(x,y))


def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)
def minkowski_distance(x,y,p_value):
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

a_list = [2, 44, 12, 6, 77]
b_list = [2, 54, 13, 15, 55]
#b_list = [2, 44, 12, 6, 77]


print("euclidean_distance : ")
print(euclidean_distance(a_list,b_list))
print("----------------------------------")

print("manhattan_distance : ")
print(manhattan_distance(a_list,b_list))
print("----------------------------------")

print("minkowski_distance : ")
print(minkowski_distance(a_list,b_list, 3))
print("----------------------------------")
