#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
sys.path.append("../")

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.chaohu.gov.cn/chwhgb/Article/lists/cateid/3.html"
		self.website = "http://www.chaohu.gov.cn"
		self.name = "[巢湖市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("ul", {"id":"article_list_page"}).find("li")
		title = tr.find("a").string
		href = tr.find("a")["href"]
		time = tr.find("span").get_text()
		msg.append((time, self.name+title, self.website + href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
