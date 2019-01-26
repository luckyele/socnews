#!/usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url ="http://wgx.fy.gov.cn/content/channel/5c3d45bf171ed55346923ce0/"
		self.website = "http://wgx.fy.gov.cn/"
		self.name = "[阜阳市]"

		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"listright-box"}).findAll("li")
		title = tr[0].find("a").string
		href = tr[0].find("a")["href"]
		time = tr[0].find("span").string
		msg.append((time, self.name+title, self.website + href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
