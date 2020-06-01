# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 07:04:16 2019

@author: Robert
"""
from vec import Vec

def zero_vec(D):
    """Returns a zero vector with the given domain
    """
    return Vec(D, {})

def list2vec(L): 
    """
    Input: a list of field elements
    Output: an instance of Vecwith domain {0...len(L)-1} such that v[i]=L[i]
    """
    return Vec(set(range(len(L))),{x:y for x,y in enumerate(L)})

def create_voting_dict(strlist):
    """ 
    input: a list of senator data strings (from a voting record file; 
    use open('xxx.txt').read().splitlines() to separate each line 
    into a properly formatted string (I really could just pass the file here)
    
    output: a dictionary that maps each senator to his/her voting record,
    where voting record is a list of ints -1, 0 or 1.
    """
    
    voting_records = dict()
    for line in strlist:
        senator_list = line.split()
        for index, item in enumerate(senator_list):
            if index > 2:
                senator_list[index] = int(item)
        voting_records[senator_list[0]] = senator_list[3:]
        
    return voting_records

def policy_compare(sena,senb,voting_dict):
    """
    input: two names of senators and a dictionary mapping senator names to 
    lists that represent voting records.
    output: dot product representing the degree of similarity in the two 
    senator's voting record. positive = agreement, negative = disagreement 
    """
    sena_list = voting_dict[sena] #get lists
    senb_list = voting_dict[senb]
    sena_vec = list2vec(sena_list) #convert to vec's
    senb_vec = list2vec(senb_list)
    agree = sena_vec*senb_vec #dotproduct
    return agree
           
def most_similar(sen,voting_dict):
    """
    input: senator name and dictionary that maps names to voting records
    output: name of senator who votes most similarly to senator input
    """
    voting_comparison = dict() #create dict for name:score
    for colleague in voting_dict.keys():
        if colleague != sen:
            voting_comparison[colleague] =  policy_compare(sen, colleague,
                             voting_dict)
    k= list(voting_comparison.keys()) #list of keys
    v = list(voting_comparison.values()) #list of values
    max_index = v.index(max(v)) #index where max value occurs
    return(k[max_index]) #key where max occurs
    
def least_similar(sen,voting_dict):
    """
    input: senator name and dictionary that maps names to voting records
    output: name of senator who votes least similarly to senator input
    """
    voting_comparison = dict() #create dict for name:score
    for colleague in voting_dict.keys():
        if colleague != sen:
            voting_comparison[colleague] =  policy_compare(sen, colleague,
                             voting_dict)
    k= list(voting_comparison.keys()) #list of keys
    v = list(voting_comparison.values()) #list of values
    min_index = v.index(min(v)) #index where min value occurs
    return(k[min_index]) #key where min occurs
    
def find_average_similarity(sen, sen_set,voting_dict):
    """
    inputs: a senators name, the list of senators and a dictionary mapping
    senators to their voting records.
    output: an integer that represents the average similarity of voing
    """
    dot_list = []
    for colleague in sen_set:
        if colleague !=sen:
            dot_list.append(list2vec(voting_dict[sen])*list2vec(voting_dict[colleague]))
    return round(sum(dot_list)/len(dot_list),2)

def find_average_record(sen_set,voting_dict):
    """
    inputs: the list of senators and a dictionary mapping senators to
    their voting records.
    output: a vector whose dictionary maps the vote element 
    to its average value
    """
    prototype = list2vec(voting_dict[sen_set[0]])
    total = zero_vec(prototype.D)
    for sen in sen_set:
        total+=list2vec(voting_dict[sen])
    avg_vec = total/len(sen_set)
    return avg_vec

def bitter_rivals(voting_dict):
    """
    input: A voting dictionary of senators and their voting records
    output: The names of the two senators who most weakly correlate
    as per the dot product of their records
    """
    lowest = float("inf") #lowest dot product
    bitter_pair= []
    sen_list = list(voting_dict.keys())
    for k in voting_dict.keys():
        for sen in sen_list:
            if sen !=k:
                dot=list2vec(list(voting_dict[sen]))*list2vec(
                    list(voting_dict[k]))
                if dot < lowest:
                    lowest = dot
                    bitter_pair = [sen,k]
    return (bitter_pair)