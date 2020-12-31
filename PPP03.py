# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:43:50 2020

@author: matth
"""


from math import floor, sqrt

if __name__ == "__main__":
    x = sqrt(2)
    y = 2 + x
    a = list()
    b = list()
    for i in range(1, 30):
        a.append(floor(x*i))
        b.append(floor(y * i))

    print(a, "\n")
    print(b)
