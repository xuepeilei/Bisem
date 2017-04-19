'''
Created on 2017年4月5日

@author: xue

重构bigram模型语料库

例子:analysis is often described as  1991  1   1   1
列名:ngram  year  match_count  page_count  volume_count
含义:In 1991, the phrase "analysis is often described as" occurred one time, and on one page, and in one book.

'''
from DB.csv_denoise import *
from DB.com import *

bigram_filter=csv_filter("E:/clp/corpora/old/bigram.csv",2)
bigram=merge(bigram_filter, 2)
    
#将二元匹配对数据导入到bigram数据库

for i in bigram:
    bigram_insert="insert into bigram(FIRST,SECOND,FREQUENTNESS) values('%s','%s','%d')"%(i[0],i[1],i[2])
    cursor.execute(bigram_insert)
connect.commit()
    
        