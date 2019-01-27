#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys
# sys.path.append("../")

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://wgxj.xuancheng.gov.cn/content/channel/56668588c6852ad6717e6d9e/"
		self.website = "http://wgxj.xuancheng.gov.cn"
		self.name = "[宣城市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find('td',{"class":"rightnr"}).find("ul", {"class":"is-listnews"}).li
		title = tr.find("a")['title']
		href = tr.find("a")["href"]
		time = tr.span.string[1:-1]
		msg.append((time, self.name+title, self.website+href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
