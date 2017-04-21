'''
Created on 2017年4月19日

@author: xue

批量化处理语料库文件
'''
import os
import platform
from DB.ngramDB import *


def batch(address,n):
#corpus_path为语料库路径
    corpus_path=os.path.join(os.getcwd(),"../corpus/")
    corpus_path=os.path.join(corpus_path,address)

    corpus_list=os.listdir(corpus_path)
    
    for i in corpus_list:
        #zip_path为zip包路径，csv_path为csv文件路径
        zip_path=corpus_path+"/"+i
        csv_path=os.path.splitext(zip_path)[0]
        #判断操作系统
        if platform.system()=="Windows":
            exe_unzip="expand "+zip_path
            exe_del="del "+csv_path
        elif platform.system()=="Linux":
            exe_unzip="unzip "+zip_path+" -d "+corpus_path
            exe_del="rm -rf "+csv_path
            
        #解压zip文件
        os.system(exe_unzip)
        
        #执行重构
        reconfiguration(csv_path,n)
          
        #删除csv文件
        os.system(exe_del)
    


    
