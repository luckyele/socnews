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
		self.url = "http://wgxj.chizhou.gov.cn/content/channel/56d555c7a70f2ed08554ff17/"
		self.website = "http://wgxj.chizhou.gov.cn"
		self.name = "[池州市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find('td',{"class":"rightnr"}).find("ul", {"class":"is-listnews"}).li
		title = tr.find("a")['title']
		href = tr.find("a")["href"]
		time = tr.span.string[1:-1]
		msg.append((time, self.name+title, self.website + href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
