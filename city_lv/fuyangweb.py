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
		self.url = "http://www.fywgxj.gov.cn/list.php?id=9"
		self.website = "http://www.fywgxj.gov.cn/"
		self.name = "阜阳市"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.findAll("td", {"class":"list_title_l"})
		title = tr[1].find("a").string
		href = tr[1].find("a")["href"]
		time = obj.findAll("td", {"class":"list_title_r"})[1].string
		msg.append((time, self.name+title, self.website + href))
	#	print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
