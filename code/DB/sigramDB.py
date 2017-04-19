'''
Created on 2017年4月19日

@author: xue
重构sigram语料库
'''
from DB.csv_denoise import *
from DB.com import *    

sigram_teamList=csv_filter("E:/clp/corpora/old/sigram.csv",1)
sigram=merge(sigram_teamList,1)

for i in sigram:
    sigram_insert="insert into sigram(FIRST,FREQUENTNESS) values('%s','%d')"%(i[0],i[1])
    cursor.execute(sigram_insert)
connect.commit()
