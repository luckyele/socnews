#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup

import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("../")

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://wlw.mas.gov.cn/4716617.html"
		self.website = "http://wlw.mas.gov.cn/"
		self.name = "[马鞍山市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj, i=1):
		msg = []
		tr = obj.find("ul", {"class":"doc_list list-4716617"})\
                .findAll("li")
		title = tr[i].a['title']
		href = tr[i].a["href"]
		time = tr[i].find("span", {"class":"right date"}).string
		msg.append((time, self.name+title, href))
		#print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
