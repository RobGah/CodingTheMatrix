# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 06:44:25 2020

@author: Robert
"""
from vec import Vec
#Quiz 4.1.1
[[0 for x in range(4)] for y in range(3)]

#Quiz 4.1.2
[[i-j for i in range (3)] for j in range(4)]

#Quiz 4.1.4
Vec({'a','b'},{'a':3,'b':30})

#rowdict
{'a': Vec({'#','@','?'},{'#':1,'@':2,'?':3}),
           'b': Vec({'#','@','?'},{'#':10,'@':20,'?':30})}
#Quiz 4.1.5 - coldict
{'@':Vec({'a','b'},{'a':1,'b':10}),'#':Vec({'a','b'},{'a':2,'b':20}),
         '?':Vec({'a','b'},{'a':3,'b':30})}

#first Mat class def
class Mat:
    def __init__(self,labels,function):
        self.D = labels
        self.f = function

M = Mat(({'a','b'},{'@','#','?'}),{('a','@'):1,('a','#'):2,('a','?'):3,
         ('b','@'):10,('b','#'):20,('b','?'):30})
