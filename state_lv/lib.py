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
		self.url = "http://www.nlc.cn/newtsgj/yjdt/"
		self.website = "http://www.nlc.cn"
		self.name = "[国家图书馆]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.findAll("a", {"class":"a-content3"})
		for a in tr:
			print(a)	
#		title = tr.find("a")["title"]
#		href = tr.find("a")["href"]
#		time = tr.next_sibling.next_sibling.string
#		msg.append((time, title, href))
#		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	web.get_newest_message(obj)

if __name__ == "__main__":
	test3()
