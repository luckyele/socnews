#!/usr/bin/python3
#coding:utf-8

from bs4 import BeautifulSoup
import os 
import pdb

FILE = 'msg.txt'
HTML = 'base.html'
HTML2 = 'ahcnews.html'

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
			msg.append((title,url,date))
			i = 0
	f.close()
	return msg

def write_html(msg):
	f = open(HTML,"r")
	h = open(HTML2, "w")
	
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()
	original_tag = soup.find("div", class_="box4")

	for title, url, date in msg:
		new_li_tag = soup.new_tag("li")
		new_a_tag = soup.new_tag("a", href=url)
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



if __name__ == "__main__":
	
	f = open(FILE,"r")
	m = get_msg(f)
	write_html(m)
