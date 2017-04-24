# 栢森（Bisem）中文语义查错系统
# <h2>程序由两部分构成：</h2>
第一部分：构建语义语料库，其中包含了构建名词动词搭配语料库和构建知网义原语料库；</br>
数据来源：</br>
1.[GoogleBooksNgramViewer](http://storage.googleapis.com/books/ngrams/books/datasetsv2.html) </br>
2.[旧版知网义原语料库](http://download.csdn.net/detail/firparks/9814417)</br>
第二部分：构建语义级查错模块，其主要是利用知网义原语料库进行动词名词抽取，并判断义项是否存在义原搭配关系，给出待纠错的位置；</br>
第三部分：构建web访问模块，其中主要是利用web.py框架进行设计。</br>

<h2>部署流程</h3>
1.下载：</br>
wget https://codeload.github.com/xuepeilei/Bisem/zip/master
</br>
2.解压：</br>
unzip Bisem-master.zip -d ~/
</br>
3.切换到执行目录：</br>
cd ~/Bisem/code/
</br>
4.设置Python环境变量：</br>
export PYTHONPATH=$PYTHONPATH:~/Bisem/code/
</br>
5.创建数据库文件(请替换"mysql_password"为你的MYSQL数据库的密码)并输出日志到~/Bisem/log/bisem.log文件：</br>
nohup python createDB.py mysql_password > ../log/bisem.log 2>&1 &
</br>
6.漫长的等待(1核2G跑1.5h)
</br>
7.更改程序中数据库连接文件(替换用户名&密码)：</br>
vim ./DB/com.py</br>
8.运行web服务器：</br>
nohup python runServer.py >> ../log/bisem.log 2>&1 &
</br>
9.访问页面：</br>
在浏览器内输入：http://服务器IP:8080
</br>
另：</br>
错误1：ModuleNotFoundError: No module named 'xxx'</br>
解决1：export PYTHONPATH=$PYTHONPATH:~/Bisem/code/
</br>
注：</br>
程序中使用的python版本为python2.7</br>
程序中使用的第三方包(如果本地没有,请使用pip安装)：jieba pymysql web.py</br>
程序中两个重要文件的位置：~/Bisem/code/createDB.py  ~/Bisem/code/runServer.py </br>


<h2>测试用例</h2>
错误语句：那个男人戴着帽子和鞋子出门了</br>
查错语句：那个男人<font color="red">戴</font>着帽子和<font color="red">鞋子出门</font>了</br>