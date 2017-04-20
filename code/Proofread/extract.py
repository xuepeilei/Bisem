# -*- coding: UTF-8 -*- 
'''
Created on 2017年4月5日

@author: xue

抽取句子中的动词-名词搭配对

待解决：包装成函数，接收句子，返回dict_1和dict_2两组搭配对

'''

import jieba.posseg as pseg

def extract(sentence):
    #切分并标注
    words=pseg.cut(sentence)
    
    v=[]
    vnc=[]
    dict_1={}
    dict_2={}
    
    #将动词、名词、连词全部抽取出来
    for w in words:
        if w.flag=="v" or w.flag=="n" or w.flag=="c":
            vnc.append(w)
    for i in range(vnc.__len__()):
        if vnc[i].flag=="v":
            v.append(i)
         
    
    #正向匹配:动词后面的名词抽取最远的一个
    for i in range(v.__len__()):
        #在两个动词之间进行匹配
        if i<v.__len__()-1:
            for j in range(v[i+1]-1,v[i],-1):
                if vnc[j].flag == "n":
                    dict_1[vnc[v[i]].word]=vnc[j].word
                    #动词前后有连词则将连词前后的名词全部抽取
                    if vnc[j-1].flag == "c" and vnc[j-2].flag == "n":
                        dict_2[vnc[v[i]].word]=vnc[j-2].word
                    break
        #在最后一个动词之后进行匹配   
        else:
            if vnc.__len__()-1>v[i]:
                for k in range(vnc.__len__()-1,v[i],-1):
                    if vnc[k].flag == "n":
                        dict_1[vnc[v[i]].word]=vnc[k].word
                        if vnc[k-1].flag == "c" and vnc[k-2].flag == "n":
                            dict_2[vnc[v[i]].word]=vnc[k-2].word
                        break  
    
    
    #逆向匹配:动词前面的名词抽取最近的一个
    for l in range(v.__len__()-1,-1,-1):
        if l>0:
            for m in range(v[l]-1,v[l-1],-1):
                if vnc[m].flag == "n":
                    dict_1[vnc[m].word]=vnc[v[l]].word
                    if vnc[m-1].flag == "c" and vnc[m-2].flag == "n":
                        dict_2[vnc[m-2].word]=vnc[v[l]].word
                    break
            
        else:
            if v[l]>0:
                for n in range(v[l]-1,-1,-1):
                    if vnc[n].flag == "n":
                        dict_1[vnc[n].word]=vnc[v[l]].word
                        if vnc[n-1].flag == "c" and vnc[n-2].flag == "n":
                            dict_2[vnc[n-2].word]=vnc[v[l]].word
                        break
                    
    list_dict=[]
    list_dict.append(dict_1)
    list_dict.append(dict_2)
    
    
    return(list_dict)
    
    
        
        
        
        
        
        
        
        
        
        