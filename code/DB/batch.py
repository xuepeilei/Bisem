# -*- coding: UTF-8 -*- 
'''
Created on 2017年4月19日

@author: xue

批量化处理语料库文件
'''
import os
import platform
from DB.ngramDB import *


def batch(address,n):
#列出路径下文件
    corpus_path=os.path.join(os.getcwd(),"../corpus/")
    corpus_path=os.path.join(corpus_path,address)

    corpus_list=os.listdir(corpus_path)
    
    for i in corpus_list:
        #找到csv文件路径
        exe_path=corpus_path+"/"+i

        #判断操作系统
        if platform.system()=="Windows":
            exe_unzip="expand "+exe_path
            exe_del="del "+exe_path
        elif platform.system()=="Linux":
            exe_unzip="unzip "+exe_path+" -d "+corpus_path
            exe_del="rm -rf "+exe_path
            
        #解压zip文件
        os.system(exe_unzip)
        
        #执行重构
        reconfiguration(exe_path,n)
          
        #删除csv文件
        os.system(exe_del)
    


    
