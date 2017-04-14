'''
Created on 2017年4月14日

@author: xue

返回互信息MI值
'''
from corpora.database.com import *

#
def mi(x,y):
    
    bigram_mi="select MI from bigram where first='%s' and second='%s'"%(x,y)
    cursor.execute(bigram_mi)
    result=cursor.fetchone()
    if result:mi=result[0]
    else:mi=0
    
    return(mi)
    