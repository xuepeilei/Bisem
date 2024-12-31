'''

@author: xue
'''
import os
import sys
from DB.batch import *
from DB.sensesDB import *
from DB.sememeDB import *


if __name__ == "__main__":
    
    #执行路径
    corpus_path=os.path.join(os.getcwd(),"../corpus/")
    sql_path=os.path.join(corpus_path,"mysql_struct.sql")
    sigram_path=os.path.join(corpus_path,"sigram")
    bigram_path=os.path.join(corpus_path,"bigram")
    senses_path=os.path.join(corpus_path,"hownet.txt")
    
    #执行数据库导入
    db='mysql -u root -p"%s" < "%s"'%(sys.argv[1],sql_path)
    os.system(db)
    
    #重构语料库
    batch(sigram_path,1)
    batch(bigram_path,2)
    senses(senses_path)
    sememe()
