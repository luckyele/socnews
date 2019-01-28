#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

import sys
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("../")

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.ahlib.com/v-AhLibWeb-zh_CN-/AhLibWeb/mian.w?mainid=4"
		self.website = "http://www.ahlib.com/"
		self.name = '[安徽省图书馆]'
		super().__init__(self.url, self.website)

	def get_obj(self):
		from selenium import webdriver
		try:
			browser = webdriver.Chrome()
		except e:
			return
		
		browser.get(self.url)
		r = browser.page_source
		print(r)
		obj = BeautifulSoup(r.encode("iso-8859-1").decode('utf-8'), "html.parser")
		return obj
	
	def get_newest_message(self, obj):
		msg = []
		label = obj.find("label", {"xid":"label1"})
		print(label)
		title = tr.a['title']
		href = tr.a["href"]
		time = tr.find("span", {"class":"right date"}).string
		msg.append((time, self.name + title, href))
		#print(msg)
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
