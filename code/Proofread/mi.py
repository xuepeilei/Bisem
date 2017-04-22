'''
Created on 2017年4月14日

@author: xue

返回互信息MI值
'''
from DB.com import *
import math

#计算互信息MI值
def mi(x,y):
    
    bigram_xy='select FREQUENTNESS from bigram where FIRST="%s" and SECOND = "%s"'%(x,y)
    sigram_x='select FREQUENTNESS from sigram where FIRST="%s"'%x
    sigram_y='select FREQUENTNESS from sigram where FIRST="%s"'%y
    cursor.execute(bigram_xy)
    f_xy=cursor.fetchone()
    cursor.execute(sigram_x)
    f_x=cursor.fetchone()
    cursor.execute(sigram_y)
    f_y=cursor.fetchone()

    #平滑方法
    if f_xy==None:
        f_xy=[1]
    if f_x==None:
        f_x=[1]
    if f_y==None:
        f_y=[1]
        
    mi=math.log2(f_xy[0]/(f_x[0]*f_y[0]))

    return(mi)
