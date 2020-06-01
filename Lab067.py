# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 06:48:39 2019

@author: Robert
"""
def makeInverseIndex(strlist):
    dct = {}
    
    docs = [i.split() for i in strlist]
    
    for iden, doc in enumerate(docs):
        for word in doc:
            if word not in dct:
                dct[word]={iden}
            else:
                dct[word].update({iden})
    return dct
                
def orSearch(inverseIndex,query):
    doc_set = set()
    
    for word in query:
        if word in inverseIndex:
            doc_set = inverseIndex[word]|doc_set 
    return doc_set

def andSearch(inverseIndex,query):
    doc_list = []
    
    for word in query:
        if word in inverseIndex:
            doc_list.append(inverseIndex[word]) #list of words w repeats
        else:
            return set() #must contain ALL words 
    doc_set = set.intersection(*doc_list) #list to intersected set
    return doc_set
