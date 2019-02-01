#!/usr/bin/python
#coding:utf-8

import itchat
import time

def send_msg(f):

	itchat.auto_login()
	itchat.send("@fil@%s"%f)
	itchat.logout()

if __name__=="__main__":
	f = 'ahcnews%s.html'%time.strftime("%Y%m%d")
	send_msg(f)
