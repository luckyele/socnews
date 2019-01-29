#!/usr/bin/python3
#coding:utf-8

from bs4 import BeautifulSoup
import os 
import pdb
import time
import itchat

import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append('../utils/')

FILE = 'msg.txt'
HTML = '../templates/base_qzone.html'
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
	a_attrs = "text-decoration:none;color:#4A4A4A;"
	a_hover_attrs = "text-decoration:underline;color:#6b6b6b;"


	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()
	original_tag = soup.find("div", class_="box")

	for title, url, date in msg:
		new_li_tag = soup.new_tag("li")
		new_li_tag['style'] = li_attrs

		new_a_tag = soup.new_tag("a", href=url)
		new_a_tag['style'] = a_attrs

		new_span_tag = soup.new_tag("span")
		new_span_tag.string = date
		new_a_tag.string = title
		
		new_li_tag.append(new_a_tag)
		new_li_tag.a.insert_after(new_span_tag)
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
