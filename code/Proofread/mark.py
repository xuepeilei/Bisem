'''
Created on 2017年4月14日

@author: xue

标记模块
'''

def mark(sentence,wrong):
    #标记
    #待解决：按次序替换出错词
    for i in wrong:
        mark_wrong='<font color="#FF0000">'+i+'</font>'
        sentence=sentence.replace(i,mark_wrong)

    #输出
    with open("/home/xue/Bisem/test.html","w") as w:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        html='<html>"%s"</html>'%sentence
        w.write(html)
