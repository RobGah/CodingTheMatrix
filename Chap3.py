# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 06:49:28 2019

@author: Robert
"""

from vec import Vec
import numpy as np

def lin_comb(vlist,clist):
    """
    input: a list of vectors vlist, a list of scalars clist
    note that the lists are to be of the same length
    
    output: the vector that is the linear combination of the vectors in
    vlist with corresponding coefficients clist
    """
    #the book wants
    #return sum([coeff*v for (coeff,v) in zip(clist,vlist)])
    
    #but I went and did
    vlist_a = np.array(vlist)
    clist_a = np.array(clist)
    return np.sum([clist_a[x]*vlist_a[x] for x in range(len(vlist_a))])
    # I cheated and used numpy because I want this thing to work with lists
    #the book solution doesn't work with basic python lists!
    
def standard(D,one): return [Vec(D,{k:one}) for k in D]