# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [dct[i] for i in keylist]

def list2dict(L, keylist): return {k:v for (k,v) in zip(keylist,L)}

def listrange2dict(L): return {i:L[i] for i in range(len(L))}