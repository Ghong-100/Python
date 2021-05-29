from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import json
import time

lastnewslist = []

class news:
    def __init__(self):
        self.m_title = ''       # [속보]김근홍 휴가쓰고싶어해. "연휴가 너무 짧다"
        self.m_time = ''        # %m-%d %H:%M
        self.m_url = ''        # https://new.ghong.co.kr/latest?12345467
    def __init__(self, title, time, url):
        self.m_title = title
        self.m_time = time
        self.m_url = url
    def print(self):
        print(f"Time : {self.m_time}\nTitle : {self.m_title}\nURL : {self.m_url}")

# --------------------------------------------
# Main Function ------------------------------

# 매경은 통합섹션이 없음...
# https://www.mk.co.kr/news/business/
# https://www.mk.co.kr/news/politics/
# https://www.mk.co.kr/news/it/
# https://www.mk.co.kr/news/society/
# https://www.mk.co.kr/news/economy/


def scrap_all(url):
    global lastnewslist
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    newsList = []
    count = 0
