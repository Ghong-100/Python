from urllib.request import *
from bs4 import BeautifulSoup
import re
# html = urlopen("https://www.asiae.co.kr/realtime/sokbo_left.htm")
# bsObject = BeautifulSoup(html, "html.parser")

# with open("BeautifulSoup\\Site\\aaa","w", encoding="utf8") as output:
# #    bsFind = bsObject.find('strong', {'class':'tit-news'}).get_text()
# #    output.write(str(bsFind))
#         output.write(str(bsObject))

# #print(bsObject)

url = 'http://m.newspim.com/lists?category_cd=1'
repattern = r"^(http(s)?:\/\/)(www\.|m\.)?([a-z0-9]+)(\.*)"
#repattern = r"^(http[s]:\/\/)(www.|m.)(*)\.*"
res = re.match(repattern, url)
print(res.group(4))

time1 = '24:59'
time2 = '10:11'

if time1 > time2:
    print(f"{time1} 이 {time2} 보다 큼")
else:
    print(f"{time1} 이 {time2} 보다 작음")