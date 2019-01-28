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
		self.url = "http://wltw.huaibei.gov.cn/gzdt/bmdt/index.html"
		self.website = "http://wltw.huaibei.gov.cn/"
		self.name = "[淮北市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		m = obj.find("ul", {"class":"doc_list list-4697572"}).li
		title = m.a["title"]
		href = m.a["href"]
		time = m.findAll("span")[1].string
		msg.append((time, self.name+title, href))
		return msg

		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
