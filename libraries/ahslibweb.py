#! /usr/lib/python
#coding:utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import re

import sys
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("../utils/")

from webmonkey import Webmonkey

class Web(Webmonkey):
	
	def __init__(self):
		# define the entrance and name of main website
		self.url = "http://www.ahlib.com/baas/ahlibWeb/AqLibApi/getListByNav"
		self.website = "http://www.ahlib.com/"
		self.name = '[安徽省图书馆]'
		super().__init__(self.url, self.website)

	def get_obj(self):
		para = {'page':1,'PageNum':15, 'RootNav':1306}
		rels = []
		surl = ""
		header = {
			"Accept":"application/json, text/javascript, */*; q=0.01",
			"Accept-Encoding":"gzip, deflate",
			"Accept-Language":"zh-CN,en-US;q=0.7,en;q=0.3",
			"Connection":"keep-alive",
			"Content-Length":"39",
			"Content-Type":"application/json",
			"Host":"www.ahlib.com",
			"Referer":"http://www.ahlib.com/v-AhLibWeb-zh_CN-/AhLibWeb/mian.w?mainid=4",
			"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:64.0) Gecko/20100101 Firefox/64.0",
			"X-Requested-With":"XMLHttpRequest",
		}
		res = requests.post(self.url, headers=header, data=json.dumps(para))
		
		print(len(json.loads(res.text)))
		if res.status_code == '200':
			print(json.loads(res))
		return rels

	def get_newest_message(self, obj):
		return obj 
		
def test3():
	web = Web()
	obj = web.get_obj()
	new = web.get_newest_message(obj)
	web.print_msg(new)

if __name__ == "__main__":
	test3()
