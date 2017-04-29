# -*- coding: utf-8 -*-
from Patient.gps import *
from Patient.mark import *

#测试函数
with open("/home/xue/Bisem/corpus/test.txt","r") as r:
    for line in r.readlines():
        wrong_set=gps(line)
        mark_sentence=mark(line,wrong_set)
        with open("/home/xue/Bisem/corpus/result.html","a") as a:
            sentence='<p>'+mark_sentence+'</p>'
            a.write(sentence)
