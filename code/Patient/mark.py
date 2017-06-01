# -*- coding: utf-8 -*-

'''
Created on 2017年4月23日

@author: lenovo
'''
import sys
reload(sys)
sys.setdefaultencoding('gbk')

def mark(sentence,wrong_list):
    #合并相同的出错词
    if wrong_list.__len__()==0:wrong_set=[]
    else:wrong_set=list(set(wrong_list))
    
    #标注
    for w in wrong_set:
        marks='<font color="#FF0000">'+w+'</font>'
        sentence=sentence.replace(w,marks)
    return(sentence)
