'''
Created on 2017年4月5日

@author: xue

构建义项语料库
'''

from corpora.database.com import *
import re

with open("E:/clp/corpora/old/hownet_mini.txt",'r') as o:
    no=[]
    w_c=[]
    g_c=[]
    define=[]
    
    #逐行匹配
    for line in o.readlines():
        if line.find("NO.")==0:
            no.append(int(line[4:].strip()))
        elif line.find("W_C")==0:
            w_c.append(line[4:].strip())
        elif line.find("G_C")==0:
            g_c.append(line[4:].strip())
        elif line.find("DEF")==0:
            sentence=line[4:].strip()
            handle=re.split(",|\|",sentence)
            define.append(handle[1::2])
    
    print("done1")
    
    #senses表和sen_def表的构建：sen_def表是senses的子表，通过NO作为外键相连
    for i in range(len(no)):
        senses_insert = "insert into senses(NO,W_C,G_C) values('%d','%s','%s')"%(no[i],w_c[i],g_c[i])
        cursor.execute(senses_insert)
        for j in range(len(define[i])):
            sen_def_insert = "insert into sen_def(NO_ID,DEF) values('%d','%s')"%(no[i],define[i][j])
            cursor.execute(sen_def_insert)

    connect.commit()
    
    print("done2")
    

    