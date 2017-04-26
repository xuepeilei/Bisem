# -*- coding: utf-8 -*-
from Proofread.corr import *

#测试函数
with open("/home/xue/Bisem/corpus/test.txt","r") as r:
    for line in r.readlines():
        corr_sentence=corr(line)
        with open("/home/xue/Bisem/corpus/result.html","a") as a:
            sentence='<p>'+corr_sentence+'</p>'
            a.write(sentence)
