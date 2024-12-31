from Patient.gps import *
from Patient.mark import *
import pymysql

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='******',
    db='bisem',
    charset='utf8'
)

cursor = connect.cursor()

#测试函数
with open("/home/xue/Bisem/corpus/correct.txt","r") as r:
    for line in r.readlines():
        wrong_set=gps(line,cursor)
        mark_sentence=mark(line,wrong_set)
        with open("/home/xue/Bisem/code/www/result.html","a") as a:
            sentence='<p>'+mark_sentence+'</p>'
            a.write(sentence)
