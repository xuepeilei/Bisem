# -*- coding: utf-8 -*-
'''
Created on 2017年4月29日

@author: lenovo
'''
from DB.com import *
from Cure.distance import *

#选出纠错词，选取与当前点距离最小的k点
def spread(first,second,k,fs):
    spread=[]
    distance_fs=[]
    candidate=[]
    #由第一项查第二项，由第二项查第一项
    if fs==0:
        fs='select FIRST from bigram where SECOND="%s" group by FIRST order by FREQUENTNESS DESC'%second
        A=first
    elif fs==1:
        fs='select SECOND from bigram where FIRST="%s" group by SECOND order by FREQUENTNESS DESC'%first
        A=second
    
    x_list=find_def(A)
    
    cursor.execute(fs)
    for i in cursor.fetchall():
        if i[0] == A:continue
        else:
            distance_fs.append(distance(x_list,i[0]))
            spread.append(i[0])
    #排序
    distance_max=sorted(distance_fs,reverse = True)
    #找到排行前k的替换词
    temp=[]
    for num in range(k):
        for i,v in enumerate(distance_fs):
            if v==distance_max[num]:
                temp.append(i)
    temp=list(set(temp))
    for i in temp:
        candidate.append(spread[i])
    return(candidate)


