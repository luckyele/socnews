#!/usr/bin/python3
#coding:utf-8

from bs4 import BeautifulSoup
import os 
import pdb
import time

import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append('../utils/')

FILE = 'msg.txt'
HTML = '../templates/base2.html'
HTML2 = 'ahcnews%s.html'%time.strftime("%Y%m%d")

def get_msg(f):
	i = 0
	date = ''
	title = ''
	url = ''
	msg=[]
	for line in f.readlines():
		if i == 0:
			date = line[0:10]
			title = line[11:].strip('\n')
			i = 1
		else:
			url = line.strip('\n')
			msg.append((title, url, date))
			i = 0
	f.close()
	return msg

def write_html(msg):
	f = open(HTML,"r")
	h = open(HTML2, "w")

	li_attrs = "list-style:none"
	a_attrs = "text-decoration:none;color:#4A4A4A"
	a_hover_attrs = "text-decoration:underline;color:#6b6b6b"


	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()
	original_tag = soup.find("div").ul

	for title, url, date in msg:
		new_li_tag = soup.new_tag("li")
		
		new_h3_tag = soup.new_tag("h3")
		
		new_img_tag = soup.new_tag("img")
		new_img_tag.string = ""
		new_h3_tag.append(new_img_tag)
		
		new_p_tag = soup.new_tag('span')
		new_p_tag.string = date
		new_li_tag.append(new_p_tag)
		new_a_tag = soup.new_tag("a", href=url, target='_blank')
		new_a_tag.string = title
		new_h3_tag.append(new_a_tag)
		
		new_li_tag.append(new_h3_tag)
		
		original_tag.append(new_li_tag)
		
	print(soup)

#	pdb.set_trace()	
	h.write(str(soup))
	h.close()

def send_msg(f):
	itchat.auto_login()
	itchat.send("@fil@%s"%f)
	itchat.logout()

if __name__ == "__main__":
	
	f = open(FILE,"r")
	m = get_msg(f)
	write_html(m)
	#send_msg(HTML2)
