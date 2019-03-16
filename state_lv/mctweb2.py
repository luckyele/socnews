#-*- coding:utf-8 -*-
#!/usr/bin/python3

import sys
sys.path.append("../")

from sqlhelper import sqlhelper1
from bs4 import BeautifulSoup
import requests


class Web:
    def __init__(self):
        self.bsObj = None
    def open(self, page_url):
        r = requests.get(page_url)
            # requests package guess encoding content of page_url, sometime it will
            # be wrong. so must set response encoding to 'utf-8'
        r.encoding = 'utf-8'
        self.bsObj = BeautifulSoup(r.text, "html.parser")
        return self.bsObj

    def find(self):
        pass

    def save(self, rows):
        db = "web_mct.db"
        tb = "ggwh"

        sql = sqlhelper1.SQLite(db, tb)
        sql.create_table()

        for row in rows:
            r = "\"%s\",\"%s\""%(row[0],row[1])
            sql.insert_record(r)

        sql.select_all()
        sql.close()

def test():
    rows=[] 
    row = []

    web_site = "http://www.mct.gov.cn/" 
    page_url = "http://www.mct.gov.cn/whzx/bnsj/ggwhs"
    w = Web()
    obj = w.open(page_url)
    tb =  obj.find("table", class_="lm_tabe")
    articles = tb.find_all("tr")

    for article in articles:
        row.append(web_site + article.td.a['href'][2:])
        row.append(article.td.a['title'])
        rows.append(row)
        row = []

    w.save(rows)

if __name__ == "__main__":
    test()
