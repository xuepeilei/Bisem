'''
Created on 2017年4月13日

@author: xue
'''
import os
from Proofread.extract import *
from Proofread.pd import *
from Proofread.mi import *
from Proofread.mark import *

#纠错模块
def corr(sentence):
    
    #名词-动词抽取
    sentence_extract=extract(sentence)
    
    #遍历所有搭配对
    wrong=[]
    i=0
    for j in sentence_extract[i].items():

        #判断互信息MI是否小于τ
        if mi(j[0],j[1])<0:
            #判断聚合度PD是否小于λ
            if pd(syn(j[0]),j[1]) < 1:
                wrong.append(j[0])
                wrong.append(j[1])
        i=1
        
    #合并相同的出错词,并标记
    wrong_set=list(set(wrong))
    mark(sentence,wrong_set)
    

if __name__ == "__main__":
    result=corr("那个男人戴着帽子和鞋子出门了。")

    