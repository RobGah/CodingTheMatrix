# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 07:35:25 2019

@author: Robert
"""

class Vec:
    def __init__ (self,labels,function):
        self.D = labels
        self.f = function
        
def setitem(v,d,val): v.f[d] = val
        
def getitem(v,d): return v.f[d] if d in v.f else 0

def scalar_mul(v,alpha): 
    return Vec(v.D,{d: value*alpha for d,value in v.f.items()})

def add(u,v): return Vec(v.D,{d:getitem(v,d)+getitem(u,d) for d in v.D})

def neg(v): return Vec(v.D,{d:-getitem(v,d) for d in v.D})

def list_dot(u,v): return sum([u[i]*v[i] for i in range(len(u))])

def dot_product_list (needle,haystack):
    """input: 
        needle: a short list of numbers
        haystack: a long list of numbers(longer than needle)
        
        output:
        a list of dot products length len(haystack)-len(needle) that 
        gives the dot product of needle and haystack when needle starts
        at the ith position of haystack
    """
    diff = len(haystack)-len(needle)
    output = []
    for i in range(diff+1):
        output.append(list_dot(needle,haystack[i:i+len(needle)]))
    return output

def list2vec(L): 
    """Input: a list of field elements
    Output: an instance of Vecwith domain {0...len(L)-1} such that v[i]
    =L[i]"""
    return Vec(set(range(len(L))),{x:y for x,y in enumerate(L)})

def zero_vec(D):
    """Returns a zero vector with the given domain
    """
    return Vec(D, {})

def triangle_solve_n(rowlist,b):
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x