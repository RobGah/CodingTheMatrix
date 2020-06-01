# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 06:48:47 2019

@author: Robert
"""
#exercise 2.6.1
#could use y=mx+b...
u = [2,3]
v = [5,7]
seg = [v[0]-u[0],v[1]-u[1]] #delta x, delta y or [3,4]
#just add [2,3] to translate segment [[0,0],[3,4]] to u,v
seg_trans = [seg[0]+2,seg[1]+3]

#exercise 2.6.2
#give expression for points making up line seg uv...aka y=mx+b
u = [1,4]
v = [6,3]
m = (u[1]-v[1])/(u[0]-v[0])
#get b
b = u[1]-m*u[0]
#anything that falls along y = 0.2x+4.2 is a valid point within seg uv

#task 2.6.9
#had trouble here at first...looked online for a solution
#realized I forgot to use add2 on the 2 halves of the convex expression
#online solution is commented out...is congruent with my solution.

def scalar_vector_mult(alpha,v): return [alpha*v[i] for i in range(len(v))]
def add2(v,w): return[v[0]+w[0],v[1]+w[1]]

def segment(pt1,pt2): return [add2(scalar_vector_mult((alpha/100),pt1),
           scalar_vector_mult((1-(alpha/100)),pt2)) for alpha in range(101)]
pt1 = [3.5,3]
pt2 = [0.5,1]
hundo_good = segment(pt1,pt2)

#def segment (pt1,pt2):
#    pts = []
#    for alpha in range(101):
#        x = (alpha/100)*pt1[0]+ (1-(alpha/100))*pt2[0]
#        y = (alpha/100)*pt1[1] +(1-(alpha/100))*pt2[1]
#        pts.append([x,y])
#    return pts
#hundo = segment(pt1,pt2)
