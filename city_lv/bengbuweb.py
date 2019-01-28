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
		self.name = '[蚌埠市]'
		self.url = "http://wgxj.bengbu.gov.cn/sitefiles/services/cms/page.aspx?s=1&n=9"
		self.website = "http://wgxj.bengbu.gov.cn"

	def get_newest_message(self, obj, index=1):
		msg = []
		tr = obj.find("div", {"class":"contain_page"}).findAll("div",\
                {"class":"list_content"})[index].findAll("div")
		title = tr[0].a.get_text()
		href = tr[0].a["href"]
		time = tr[1].get_text()[5:]
		msg.append((time, self.name + title, self.website+href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
