'''
Created on 2017年4月5日

@author: xue

构建义项语料库
'''

from DB.com import *
import re


def senses(address):
    regex=re.compile('[^\u4E00-\u9FA5]')
    with open(address,'r',encoding='utf-8') as r:
        #no:编号 w_c:词 g_c:词性 define:义原
        no=[]
        w_c=[]
        g_c=[]
        define=[]
        
        #逐行匹配
        for line in r.readlines():
            if line.find("NO.")==0:
                no.append(int(line[4:].strip()))
            elif line.find("W_C")==0:
                w_c.append(line[4:].strip())
            elif line.find("G_C")==0:
                g_c.append(line[4:].strip())
            elif line.find("DEF")==0:
                sentence=line[4:].strip()
                handle=re.split(",|\|",sentence)
                #找到中文以及中文字符
                define.append(handle[1::2])
        
        
        #senses表和sen_def表的构建：sen_def表是senses的子表，通过NO作为外键相连
        for i in range(len(no)):
            senses_insert = 'insert into senses(NO,W_C,G_C) values(%d,"%s","%s")'%(no[i],w_c[i],g_c[i])
            cursor.execute(senses_insert)
            for j in range(len(define[i])):
                #提取义原中的中文成分
                define_sub=regex.sub("",define[i][j])
                sen_def_insert = 'insert into sen_def(NO_ID,DEF) values(%d,"%s")'%(no[i],define_sub)
                cursor.execute(sen_def_insert)
    
        connect.commit()

    

    