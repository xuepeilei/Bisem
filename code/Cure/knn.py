# -*- coding: utf-8 -*-
'''

@author: lenovo

KNN纠错方式
'''
from DB.com import *
from Cure.distance import distance
from Cure.spread import spread

def knn(wrong_list):
    cure_sentence=[]
    
    for i in range(0,wrong_list.__len__(),2):
        #拓展词集
        candidate_f=spread(wrong_list[i],wrong_list[i+1],3,0)
        candidate_s=spread(wrong_list[i],wrong_list[i+1],3,1)
        cure_sentence.append(display(wrong_list[i],candidate_f))
        cure_sentence.append(display(wrong_list[i+1],candidate_s))

    return(cure_sentence)


def display(wrong,candidate):
    result=""
    for i in candidate:
        result=result+i+","
    result="|"+wrong+"|"+" "+"-->"+" "+result
    return(result)










