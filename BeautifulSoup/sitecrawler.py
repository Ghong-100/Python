from urllib.request import *
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, re
import datetime, time
import time
import sys, inspect
import json


url = "https://www.news1.kr/latest/"
url = "https://rest.news1.kr/w/ajax/extcontent?type=breaking_news"
url = "https://rest.news1.kr/archive/list"

html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

repattern = r"^(http(s)?:\/\/)(www\.|m\.|rest\.)?([a-z0-9]+)(\.*)"

res = re.match(repattern, url)
m_domain = res.group(4)
mod_name = str(m_domain)# + ".py"

# bsFind = bsObject.find('data')
#print(str(bsObject))
bsFind = json.loads( str(bsObject) )


#findData = bsFind.find_all(True, {"class": ["id","pubdate1","title"]})

#print(bsFind["data"])
for index in bsFind["data"]:
    print(index["pubdate"])

    여기 다시 잡아줘야함. 엉뚱한 주소를 보고있었네...
    print(type(index["pubdate"]))
    
    print(index["pubdate"][11:16])
    #print(index["article_id"], end=' ')
    #print(index["title"])

print(bsFind["data"][0])
#with open(m_domain+".html","w", encoding="utf8") as output:
    #for ou in bsFind["data"]:
        #output.write(ou)

#        output.write(str(bsObject))
#print(bsObject)