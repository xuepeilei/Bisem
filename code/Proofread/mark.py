# -*- coding: utf-8 -*-
'''
Created on 2017年4月23日

@author: lenovo
'''
def mark(sentence,wrong_set):
    for w in wrong_set:
        marks='<font color="#FF0000">'+w+'</font>'
        sentence=sentence.replace(w,marks)
    return(sentence)