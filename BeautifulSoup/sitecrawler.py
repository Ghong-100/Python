from urllib.request import *
from bs4 import BeautifulSoup
from bs4 import element
from urllib.request import urlopen
import os, re
import datetime, time
import time
import sys, inspect
import json


url = "https://www.mk.co.kr/news/all/"

html = urlopen(url)
bsObject = BeautifulSoup(html, "html.parser")

repattern = r"^(http(s)?:\/\/)(www\.|m\.|rest\.)?([a-z0-9]+)(\.*)"

res = re.match(repattern, url)
m_domain = res.group(4)
mod_name = str(m_domain)# + ".py"

## mk
# <div class="list_area">
#bsFind = bsObject.findAll("div", {"class":"list_area"})
bsFind = bsObject.find("div", attrs={"class": ["list_area"]})

# print(bsFind)


findData = bsFind.find_all(True, {"class": ["tit","date"]})


for idx in range(0, len(findData)):
    if idx%2 == 0:
        print( findData[idx].get_text() )        # 짝수번째의  일반 텍스트는  title
        print( findData[idx].find('a')['href'] ) # 짝수번째의  a태크의 href는 url
    else:
        print( findData[idx].get_text() )        # 홀수번째의  일반 텍스트는  time
        pass

# for line in findData:
#     index += 1
#     print(line)
#     print(line.get_text())
    #aa = line.find('a')
    #print(aa['href'])

    # for l in line:
    #     print("LL")
    #     print(type(l))
    #     print(l)
    #     print(l["href"])
#bf2 = bsFind.findAll()
#for s in bsFind:
#    print(s.get_text() + "DDDDDDDDD")
    

#findData = bsFind.find_all(True, {"class": ["id","pubdate1","title"]})

with open(m_domain+".html","w", encoding="utf8") as output:
    output.write( str(bsObject) )
    #output.write(  )
    



''' news1
print(str(bsObject))
bsFind = json.loads( str(bsObject), strict=False )
for index in bsFind["data"]:
    # 여기 다시 잡아줘야함. 엉뚱한 주소를 보고있었네...
    #print(index["article_id"], end=' ')
    print(index["title"])
    print(index["id"])
    # print( str(index["pubdate1"]).replace("분전", "") )
    print( time.strftime('%H:%M', time.localtime(time.time() - int(str(index["pubdate1"]).replace("분전", ""))*60) ) )
print(time.strftime('%H:%M', time.localtime(time.time() - 5*60)) )
'''

### yna
# bsFind = bsObject.find('data')
# print(bsObject)
#findData = bsFind.find_all(True, {"class": ["id","pubdate1","title"]})
# print(bsFind["data"])
#print(bsFind["data"][0])
#with open(m_domain+".html","w", encoding="utf8") as output:
#    output.write( str(bsObject) )
        #output.write(ou)

#        output.write(str(bsObject))
#print(bsObject)