from urllib.request import urlopen
from bs4 import BeautifulSoup
import os, re

import sys, inspect
sys.path.append('BeautifulSoup\\site')

repattern = r"^(http(s)?:\/\/)(www\.|m\.)?([a-z0-9]+)(\.*)"

class news:
    def __init__(self):
        self.m_title = ''       # [속보]김근홍 휴가쓰고싶어해. "연휴가 너무 짧다"
        self.m_time = ''        # %m-%d %H:%M
        self.m_link = ''        # https://new.ghong.co.kr/latest?12345467

class site:
    def __init__(self, url):
        self.m_url = url
        res = re.match(repattern, url)
        self.domain = res.group(4)
        # print(self.m_url, self.domain)
        mod_name = str(self.domain)# + ".py"
        # print(mod_name)
        mod = __import__('%s' %(mod_name), fromlist=[mod_name])
        scrap = getattr(mod, 'scrap')
        scrap(url)



#############################################################################################
## Main
#############################################################################################

## Read files
site_list = []
with open("D:\\30_STUDY\\python\\BeautifulSoup\\site\\sites.txt", "r", encoding="utf8") as data:    
    '''
    while True:
        line = data.readline()
        if not line:
            break
        site_list.append(site(line))
    '''
    line = data.readline()
    site_list.append(site(line))

print("end")