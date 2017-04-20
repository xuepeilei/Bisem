# -*- coding: UTF-8 -*- 
'''
Created on 2017年4月20日

@author: xue
'''
from DB.batch import *
from DB.sensesDB import *
from DB.sememeDB import *

if __name__ == "__main__":
    batch("sigram",1)
    batch("bigram",2)
    senses("./../../corpus/hownet.txt")
    sememe()