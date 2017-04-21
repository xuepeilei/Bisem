'''
Created on 2017年4月19日

@author: xue

去噪模块
'''
import re

#筛选函数：比如“雪国    1993    1    2    3”去噪以后输出['雪国','1'] 即：['词','频数']
def csv_filter(csv_dir,n):
    result=[]
    regex=re.compile('[\u4e00-\u9FA0]')
    #打开csv文件
    with open(csv_dir,'r',encoding='utf-8') as r:
        for row in r.readlines():
            #按照空格进行切分
            context=re.split("[\s]",row.rstrip())
            #确定无残缺行
            if context.__len__() == (n+4):
                threshold=0
                for i in range(n):
                    #正则匹配中文词,并确保词的每一项都为中文
                    if re.match(regex,context[i]):
                        threshold+=1
                    else:break
                if threshold==n:
                    #将词和频数转存temp[]
                    temp=[]
                    for j in range(n):
                        temp.append(context[j])
                    temp.append(int(context[n+1]))
                        #构造二维列表
                    result.append(temp)                  
    return(result)

#待解决：改造为hadoop合并
#合并函数:例如将"[['一休', '1'], ['一休', '1']]"合并为[['一休', '2']]、
def merge(teamList,n):
    teamList_merge=[]
    for line in range(teamList.__len__()-1):
        #判断每行的词是否和下一行的词相同，相同阀值threshold为0，不同阀值threshold为1
        threshold=0
        for i in range(n):
            if teamList[line][i]!=teamList[line+1][i]:
                threshold=1
                break
        #该行和下一行词相同时，该行的词频加到下一行的词频上
        if threshold==0:
            sum_num=teamList[line+1][n]+teamList[line][n]
            teamList[line+1][n]=sum_num
        else:
            #到达下一组合并行的前一行时，将该行添加到teamList_merge[]中
            teamList_merge.append(teamList[line])
    #将最后一行加入teamList_merge[]中
    teamList_merge.append(teamList[-1])
      
    return(teamList_merge)