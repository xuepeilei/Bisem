'''
Created on 2017年4月5日

@author: xue
公共数据库头
'''

import pymysql

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='einsam@163.com',
    db='test',
    charset='utf8'
)

cursor = connect.cursor()
