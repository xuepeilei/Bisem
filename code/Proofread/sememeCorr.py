'''
Created on 2017年4月13日

@author: xue
'''
from correction.extract import *
from correction.pd import *
from correction.mi import *
from correction.mark import *

#纠错模块
def sememeCorr(sentence):
    #名词-动词抽取
    sentence_extract=extract(sentence)
    
    #遍历所有搭配对
    for i in sentence_extract[0].items():
        #判断互信息MI是否小于τ
        if mi(i[0],i[1])<0.01:
            #判断聚合度PD是否小于λ
            if pd(syn(i[0]),i[1]) < 1:
                mark(sentence,i[0],i[1])
            
     


if __name__ == "__main__":
    result=sememeCorr("那个男人戴着帽子和鞋子出门了。")

    