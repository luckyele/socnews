#! /usr/lib/python
#coding:utf-8

from bs4 import BeautifulSoup

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "https://www.mct.gov.cn/whzx/ggtz/"
		self.website = "https://www.mct.gov.cn"
		self.name = "[文旅部]"
		super().__init__(self.url, self.website)

	def get_newest_message(self, obj):
		msg = []
		tr = obj.find("div", {"class":"bt-rig-cen-01"}).find("td")
		title = tr.find("a")["title"]
		href = tr.find("a")["href"]
		time = tr.next_sibling.next_sibling.string
		msg.append((time, title, href))
		return msg
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
