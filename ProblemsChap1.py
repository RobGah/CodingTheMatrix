# -*- coding: utf-8 -*-
"""
Chapter 1 problems
Created on Fri Sep 27 06:47:30 2019

@author: Robert
"""
from math import e, pi

#Problem 1.5.1

cyphertext = ['0b10101','0b00100','0b10101','0b01011','0b11001','0b00011',
              '0b01011','0b10101','0b00100','0b11001','0b11010']


lettertonumber = {0b00000:'a',0b00001:'b',0b00010:'c',0b00011:'d',0b00100:'e',
                  0b00101:'f',0b00110:'g',0b00111:'h',0b01000:'i',0b01001:'j',
                  0b01010:'k',0b01011:'l',0b01100:'m',0b01101:'n',0b01110:'o',
                  0b01111:'p',0b10000:'q',0b10001:'r',0b10010:'s',0b10011:'t',
                  0b10100:'u',0b10101:'v',0b10110:'w',0b10111:'x',0b11000:'y',
                  0b11001:'z',0b11010:'_'}
countto32 = [bin(x) for x in range(0b100000)]

#bin converts an int to a binary string representation
#int converts binary string to a binary number when given a base-2 input

possiblelist = [] #list of all possible sums of cypher and candidate key

for x in countto32: #XOR all 32 possible 5-bit keys with the cyphertext
    possiblelist.append([bin(int(x,2)^int(y,2)) for y in cyphertext]) 
    
phrasecandidate = []
for candidate in possiblelist: #look-up candidate plaintext in letter dict
      phrasecandidate.append([lettertonumber[int(x,2)] for x in candidate 
                                             if int(x,2) in lettertonumber]) 
    #coulda had lettertonumber contain all binary strings but whatever

#print phrasecandidate...you get...
#EVE IS EVIL as a list item! 
    
#Problems 1.7.1 through 1.7.3

#1.7.1
def my_filter(L,num): return [x for x in L if x%num !=0]
#1.7.2
def my_lists(L): return [[n for n in range(x+1) if n!=0] for x in L]
#1.7.3
def my_function_composition(f,g): 
    return {k:v for (k,v) in zip([a for a in f.keys()],
                     [b for b in g.values()])}
#1.7.4 
def mySum(L):
    current = 0
    for x in L:
        current +=x
    return current
#1.7.5
def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return 
#1.7.6
def myMin(L):
    current = float('inf') #set to infinity
    for x in L:
        if x < current:
            current = x
    return current
#1.7.
def myConcat(L):
    current = '' #empty string
    for x in L:
        current += x
    return current
#1.7.8
def myUnion(L):
    current=set() #empty set
    for x in L:
        current = current|x 
    return current
#1.7.9
def myIntersection(L):
   current=set() #empty set
   for x in L:
       current = current&x  #this returns an empty set. should return nothing?
   return current

#1.7.10
a = (3+11j)+(2+2j)
b = (-1+2j)+(1-1j)
c = (2+0j)+(-3+0.001j)
d = 4*(0+2j)+(.001+1j)
#1.7.11
a = (e**1j)*(e**2j) #aka e**3j
b = (e**(pi*1j/4))*(e**(2*pi*1j/3)) #aka e**(11*1j*pi/12)
c = (e**(-pi*1j/4))*(e**(2*pi*1j/3)) #aka e**(5*1j*pi/12)

#1.7.12
def transform(a,b,L):
    f = [] #empty list
    """
    input: complex numbers a, b and a list L of complex numbers
    
    output: the list of complex number obtained by applying
    f(z)=az+b to each complex number in L
    
    """
    for z in L:
        f.append((a*z) + b)
    return f

L = [2+2j,3+2j, 1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j] #face

# A. translate one unit up, one to the right, rotate 90deg clockwise, scale 2
a = 2*e**(-pi*1j/2) #scale 2x, rotate -pi/2 or 90 degrees clockwise
b = 1+1j #translate 1 up, one right 

# B. scale real by 2 and imag by 3, rotate 45deg counter and translate 2 down
#and 3 left
a = (2+3j)*e**(pi*1j/4) #45deg clockwise 2xreal 3ximag
b = (-2j-3) #down 2, left 3