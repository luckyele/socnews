#! /usr/lib/python
#coding:utf-8

import mctweb		as mct
import anhuiweb 	as ah
import hefeiweb		as hf
import bozhouweb 	as bzh
import chuzhouweb 	as chuzh
import fuyangweb2 	as fy
import huainanweb 	as hn
import huaibeiweb 	as hb
import huangshanweb as hsh
import luanweb 		as luan
import maanshanweb 	as msh
import xuanchengweb as xch
import anqingweb 	as anq
import chizhouweb 	as chzh
import tonglingweb 	as tl
import bengbuweb 	as bb
import wuhuweb 		as wh
import suzhouweb 	as szh

def scheduling(p_area):
	web = p_area.Web()
	try:
		obj = web.get_obj()
		new = web.get_newest_message(obj)
	except:
		return
	web.print_msg(new)

def test():
	msgs = [ah,\
			hf, bzh, szh, bb,   fy,  hn,  chuzh, \
			luan, msh, wh,  tl,  chzh, anq, xch, hsh]

	for p_area in msgs:
		scheduling(p_area)

if __name__ == "__main__":
	test()
