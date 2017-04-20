# -*- coding: UTF-8 -*- 
'''
Created on 2017年4月5日

@author: xue

重构N-gram模型语料库

例子:analysis is often described as  1991  1   1   1
列名:ngram  year  match_count  page_count  volume_count
含义:In 1991, the phrase "analysis is often described as" occurred one time, and on one page, and in one book.

'''
from DB.csv_denoise import *
from DB.com import *

def reconfiguration(location,n):
    #调用去噪模块的csv_filter()函数和merge()函数
    filter_list=csv_filter(location,n)
    ngram=merge(filter_list,n)
        
    #将数据导入到bigram或者sigram数据库
    for i in ngram:
        if n==1:
            ngram_insert='insert into sigram(FIRST,FREQUENTNESS) values("%s",%d)'%(i[0],i[1])
        elif n==2:
            ngram_insert='insert into bigram(FIRST,SECOND,FREQUENTNESS) values("%s","%s",%d)'%(i[0],i[1],i[2])
        cursor.execute(ngram_insert)
    connect.commit()

        