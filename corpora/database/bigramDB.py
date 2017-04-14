'''
Created on 2017年4月5日

@author: xue

重构bigram模型语料库

例子:analysis is often described as  1991  1   1   1
列名:ngram  year  match_count  page_count  volume_count
含义:In 1991, the phrase "analysis is often described as" occurred one time, and on one page, and in one book.

'''
import csv
import re
from corpora.database.com import *
from itertools import count


temp=[]

#处理旧文件
with open('E:\clp\corpora\old\googlebooks.csv','r',encoding='UTF-8') as file:
    reader = csv.reader(file, delimiter='\t', quoting=csv.QUOTE_NONE)
    
    #去噪，去噪后的形式：  #['一' '1125' '1'] 即：'词' '词' '频数'
    for row in reader:
        if row.__len__() == 5:
            #正则匹除去含有a-zA-Z0-9以及其他非汉字
            if re.match(r"[\u4e00-\u9FA0]",row[0]) and re.match(r"[\W\D]",row[0]):
                #将二元语言模型的两个词分别切出来
                context=re.split("[\t\s]",row[0])
                context.append(int(row[2]))
                temp.append(context)
                
    print("done1")

         
    #合并相同的行,记录不同行的行号至num[]中
    #待解决：现在取1000条组成mini语料库，实际为range(len(temp))       
    num=[]   
    for line in range(4000,5000):
        if temp[line][0]==temp[line+1][0]:
            if temp[line][1]==temp[line+1][1]:
                sum_num=temp[line+1][2]+temp[line][2]
                temp[line+1][2]=sum_num
            else:
                num.append(line)
        else:
            num.append(line)
    print("done2")
    
    #统计bigram模型下的总频数
    count=0
    for i in num:
        count+=temp[i][2]
    
    
    #将二元匹配对数据导入到bigram数据库
    for j in num:
        fre=temp[j][2]/count
        google_insert="insert into bigram(FIRST,SECOND,FREQUENTNESS,FREQUENCY) values('%s','%s','%f','%f')"%(temp[j][0],temp[j][1],temp[j][2],fre)
        cursor.execute(google_insert)
    connect.commit()
    
    print("done3")
    
    #将bigram表中的first和second转到一张表中
    bi_temp="insert into bi_temp(W,F) select first,sum(FREQUENTNESS) from bigram group by FIRST UNION select SECOND,sum(FREQUENTNESS) from bigram group by SECOND"
    cursor.execute(bi_temp)
    connect.commit()
    
    print("done4")
    
    
    #进行合并同行,计算词的概率值
    bigram_summer="SELECT sum(F) from bi_temp"
    cursor.execute(bigram_summer)
    summer=cursor.fetchone()
    bi_frequentness="insert into bi_words(W,FREQUENTNESS,FREQUENCY) SELECT w,SUM(F),(SUM(F)/%f) from bi_temp GROUP BY w"%summer[0]
    cursor.execute(bi_frequentness)
    connect.commit()
    
    print("done5")
   
    #增补bigram表的互信息值：MI
    bi="select * from bigram"
    cursor.execute(bi)
    for i in cursor.fetchall():
        bi_words_select1="select FREQUENCY from bi_words where W='%s'"%i[1]
        bi_words_select2="select FREQUENCY from bi_words where W='%s'"%i[2]
        cursor.execute(bi_words_select1)
        f1=cursor.fetchone()
        cursor.execute(bi_words_select2)
        f2=cursor.fetchone()
        num=i[4]/f1[0]*f2[0]
        bigram_update="update bigram set MI = %f where id=%d"%(num,i[0])
        cursor.execute(bigram_update)
    connect.commit()
    
    print("done6")

        
        