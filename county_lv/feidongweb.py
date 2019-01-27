#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sys

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.feidong.gov.cn/orglist.asp?base_id=14&third_id=404"
		self.website = "http://www.feidong.gov.cn/"
		self.name = "[肥东县]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("ul", {"class":"list-1"}).li
		title = tr.a.string
		href = tr.a["href"]
		time = tr.find("span", {"class":"date"}).string
		msg.append((time, self.name+title, self.website + href))
		#print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
