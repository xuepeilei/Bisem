'''
Created on 2017年4月13日

@author: xue
构建义原表
'''
from corpora.database.com import cursor,connect

#将sen_def表中的义原合并导入到sememe表
sememe_insert="insert into sememe(S) select DEF from sen_def group by DEF"
cursor.execute(sememe_insert)
connect.commit()

#训练bi_words表内的词到sem_w中
bi_words_find="select * from bi_words"
cursor.execute(bi_words_find)

#遍历，其中i[1]是词
for i in cursor.fetchall():
    sen_def_find="select d.DEF from senses s,sen_def d where s.W_C='%s' and s.NO=d.NO_ID"%i[1]
    cursor.execute(sen_def_find)
    for j in cursor.fetchall():
        #从sememe表找到该词的id
        sem_id="select ID from sememe where S='%s'"%j[0]
        cursor.execute(sem_id)
        id=cursor.fetchone()
        #训练后插入到sem_w表中
        sem_w_insert="insert into sem_w(SEM_ID,SEM_W) values(%d,'%s')"%(id[0],i[1])
        cursor.execute(sem_w_insert)

connect.commit()
