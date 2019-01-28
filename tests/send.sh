#!/bin/bash


#抓取数据
python3 test.py > msg.txt

#生成网页文件
python3 txt2html.py

#发送邮件
mail -s "文化信息" 541913141@qq.com -A ahcnews`date +%Y%m%d`.html

