# 栢森（Bisem）中文语义查错系统
# <h2>程序由两部分构成：</h2>
【已完成】第一部分是构建语义语料库，其中包含了构建名词动词搭配语料库和构建知网义原语料库；</br>
数据来源：</br>
1.[GoogleBooksNgramViewer](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html) </br>
2.[旧版知网义原语料库](http://download.csdn.net/detail/firparks/9814417)</br>
【已完成】第二部分是构建语义级查错模块，其主要是利用知网义原语料库进行动词名词抽取，并判断义项是否存在义原搭配关系，给出待纠错的位置；</br>
