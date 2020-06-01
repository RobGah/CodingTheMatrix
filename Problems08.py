# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 06:59:01 2019

@author: Robert
"""

"Problem 0.8.1"
def increments(L): return [i+1 for i in L]

"Problem 0.8.2"
def cubes(L): return [i**3 for i in L]

"Problem 0.8.3"
def tuple_sum(A,B):
    #whew
    return [(A[i][0]+B[i][0],A[i][1]+B[i][1]) for i in range(len(A))]

"Problem 0.8.4"
def inv_dict(d): return {v:k for (k,v) in d.items()}            

"Problem 0.8.5"
def row(p,n): return [p+i for i in range(n)]

#[row(x,20) for x in range(15)]
#[x+i for i in range(20) for x in range(15)]
