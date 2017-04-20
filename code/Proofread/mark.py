# -*- coding: UTF-8 -*- 
'''
Created on 2017年4月14日

@author: xue

标记模块
'''
import codecs

def mark(sentence,x,y):
    mark_x='<font color="#FF0000">'+x+'</font>'
    mark_y='<font color="#FF0000">'+y+'</font>'
    sentence_x=sentence.replace(x,mark_x)
    sentence_y=sentence_x.replace(y,mark_y)
    
    with codecs.open("/home/test.html","w",'utf-8') as w:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        html='<html>"%s"</html>'%sentence_y
        w.write(html)
