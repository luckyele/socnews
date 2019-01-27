#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
from webmonkey import Webmonkey
import requests

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://whw.wuhu.gov.cn/List.aspx?pTypeID=111601"
		self.website = "http://whw.wuhu.gov.cn/"
		self.name = "[芜湖市]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"listcontent"}).find("ul",{"id":"list"}).li
		title = tr.a.get_text()[:-12].lstrip("\r\n").lstrip(" ").rstrip(" ").rstrip("\r\n")
		href = tr.a["href"]
		time = tr.find("span").string.lstrip("\r\n").lstrip(' ')
		msg.append((time, self.name+title, self.website + href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)
if __name__ == "__main__":
	test3()
