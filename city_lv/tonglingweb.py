#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup

import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("../utils/")

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://wlw.tl.gov.cn/6247/6248/6249/"
		self.website = "http://wlw.tl.gov.cn/6247/6248/6249/"
		self.name = "[铜陵市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("ul",{"class":"n-list"}).li

		title = tr.find("a")['title']
		href = tr.find("a")["href"]
		time = tr.find('span').string
		msg.append((time, self.name+title, self.website + href[2:]))
		#print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
