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
		self.url = "http://www.ahwh.gov.cn/zwgk/bmdt/"
		self.website = "http://www.ahwh.gov.cn"
		self.name ='[省厅]'.encode('GBK').decode('iso-8859-1')
		super().__init__(self.url, self.website)

	def get_newest_message1(self, obj):
		msg = []
		tr = obj.find("div", {"class":"list"}).find("div", {"class":"tr"})
		title = tr.find("div", class_="title").a["title"]
		href = tr.find("div", class_="title").a["href"]
		time = tr.find("div", class_="time").get_text()[1:-1]
		msg.append((time, self.name + title, self.website + href))
		return msg


	def get_newest_message(self, obj, index=0):
		msg = []
		tr = obj.find("div", {"class":"zwgk_right"}).findAll("div",{"class":"tr" })
		title = tr[index].find("div", class_="title").a["title"]
		href = tr[index].find("div", class_="title").a["href"]
		time = tr[index].find("div", class_="time").get_text()[1:-1]
		msg.append((time, self.name + title, self.website + href))
		return msg


	def print_msg(self, msg):
		print(msg[0][0], msg[0][1].encode('iso-8859-1').decode('GBK'))
		print(msg[0][2])

		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
