# -*- coding: UTF-8 -*- 
'''
Created on 2017年4月14日

@author: xue
计算聚合度PD值
'''

from DB.com import *
import itertools

#找到具有相同义原的词集合的函数
def syn(x):
    
    syn_list=[]
    
    #找到义原
    sen_def_x='select DEF from sen_def where NO_ID=(select NO from senses where W_C="%s")'%x
    cursor.execute(sen_def_x)
    
    #在sem_w表中找到全部词集合sem_w_synx
    for i in cursor.fetchall():
        #i[0]为义原
        sem_w_synx='select SEM_W from sem_w where SEM_ID = (select ID from sememe where S="%s")'%i[0]
        cursor.execute(sem_w_synx)
        for j in cursor.fetchall():
            syn_list.append(j[0])
            
    return(syn_list)

#计算pd的函数:x,y均为列表
def pd(x,y):
    #计算分母部分
    if x.__len__()!=0:
        n=x.__len__()
    else:
        n=1
       
    #计算两个列表的笛卡尔积，并查找bigram表是否含有搭配对
    num=0
    y_list=[]
    y_list.append(y)
    for i in itertools.product(x,y_list):
        bigram_find='select * from bigram where FIRST="%s" and FIRST="%s"'%i
        cursor.execute(bigram_find)
        #计算∑(C_(x,y))
        if cursor.fetchone():num+=1
    
    #计算PD值
    pd=float(num/n)

    return(pd)
    



    
    
    
    
    
    
    
    
