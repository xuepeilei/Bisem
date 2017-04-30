# -*- coding: utf-8 -*-
'''
Created on 2017年4月14日

@author: xue
计算聚合度PD值
'''

from DB.com import *

#找到具有相同义原的词集合的函数
def syn(x,i):
    
    if i == 0:g_c="v"
    elif i==1:g_c="n"
    
    syn_list=[]

    #找到义原
    sen_no_x='select NO from senses where W_C="%s" and G_C="%s"'%(x,g_c)
    cursor.execute(sen_no_x)
    for no in cursor.fetchall():
        sen_def_x='select DEF from sen_def where NO_ID=%d'%no[0]
        cursor.execute(sen_def_x)
        #在sem_w表中找到全部词集合sem_w_synx
        for i in cursor.fetchall():
            #i[0]为义原
            sem_w_synx='select SEM_W from sem_w where SEM_ID = (select ID from sememe where S="%s") group by SEM_W'%i[0]
            cursor.execute(sem_w_synx)
            for j in cursor.fetchall():
                syn_list.append(j[0])
               
    return(syn_list)

#计算pd的函数:x,y均为列表
def pd(x,y):
    x_set=list(set(x))
    
    #计算分母部分
    if x.__len__()!=0:
        n=x_set.__len__()
    else:
        n=1
        
    #计算两个列表的笛卡尔积，并查找bigram表是否含有搭配对
    first=[]
    bigram_find='select FIRST from bigram where SECOND="%s"'%y
    cursor.execute(bigram_find)
    for i in cursor.fetchall():
        first.append(i[0])
    #求交集
    inter=list(set(first).intersection(x_set)).__len__()
    
    #计算PD值
    pd=inter/float(n)
    return(pd)

    
    
    
    
    
    
    
