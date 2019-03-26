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
		self.url = "http://www.chinamuseum.org.cn/plus/list.php?tid=156"

		self.website = "http://www.chinamuseum.org.cn"
		self.name = "博物馆"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"zixun"}).find("ul").findAll('a')
		for a in tr:
			title = a.text
			href = a["href"]
			msg.append((title, self.website+href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	msg = web.get_newest_message(obj)
	print(msg)

if __name__ == "__main__":
	test3()
