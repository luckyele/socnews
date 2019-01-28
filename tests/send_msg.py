#!/usr/bin/python
#coding:utf-8

import itchat

def send_msg(f):

	itchat.auto_login()
	itchat.send("@fil@%s"%f)
	itchat.logout()

if __name__=="__main__":
	f = "ahcnews.html"
	send_msg(f)
