# -*- coding: utf-8 -*-
'''
Created on 2017年4月13日

@author: xue
'''
import os
from Patient.extract import *
from Patient.pd import *
from Patient.mi import *

#纠错模块
def gps(sentence):
    
    #名词动词搭配对抽取
    sentence_extract=extract(sentence)
    
    #遍历所有搭配对
    wrong=[]
    i=0
    for j in sentence_extract[i].items():
        #判断互信息MI是否小于τ
        if mi(j[0],j[1])<1:
            #判断聚合度PD是否小于λ
            if pd(syn(j[0],i),j[1]) < 1:
                wrong.append(j[0])
                wrong.append(j[1])
        i=1
    
    return(wrong)

    