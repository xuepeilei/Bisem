# -*- coding: utf-8 -*-
'''
Created on 2017年4月29日

@author: lenovo

计算搭配对之间的距离
'''
from DB.com import *
import math

#计算距离
def distance(x_list,y):
    y_list=find_def(y)
    #合并义原
    denominator=list(set(x_list+y_list)).__len__()    
    numerator=list(set(x_list).intersection(y_list)).__len__()
    
    #正弦
    d=math.sin(numerator/float(denominator))
    return(d)

#找到词的相应的义原NO
def find_def(words):
    sememe_list=[]

    senses_no='select NO from senses where W_C="%s" and (G_C="N" or G_C="V")'%words
    cursor.execute(senses_no)
    for i in cursor.fetchall():
        senses_def='select DEF from sen_def where NO_ID=%d'%int(i[0])
        cursor.execute(senses_def)
        for j in cursor.fetchall():
            sememe_list.append(j[0])
    sememe_list=list(set(sememe_list))
    return(sememe_list)

