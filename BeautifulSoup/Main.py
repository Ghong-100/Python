##################################
#   Autor : Ghong Kim.
#   mail : ghd644@gmail.com
#
#  Version
#   python          3.8.0
#   BeautifulSoup   4.9.1
#   PyQt5           5.15.0
#################################

from urllib.request import urlopen
from bs4 import BeautifulSoup

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5 import uic

import telegram

import os, re, sys
import datetime, time, inspect, webbrowser

sys.path.append('BeautifulSoup\\site')
sys.path.append('D:\\30_STUDY\\Python\\BeautifulSoup\\site')

class news:
    def __init__(self):
        self.m_title = ''       # [속보]김근홍 휴가쓰고싶어해. "연휴가 너무 짧다"
        self.m_time = ''        # %m-%d %H:%M
        self.m_url = ''        # https://new.ghong.co.kr/latest?12345467
    def print(self):
        print(f"Time : {self.m_time}\nTitle : {self.m_title}\nURL : {self.m_url}")

class site:
    def __init__(self, url):                    # rest는 new1이 rest로 시작해서임
        repattern = r"^(http(s)?:\/\/)(www\.|m\.|rest\.)?([a-z0-9]+)(\.*)"
        self.m_url = url
        res = re.match(repattern, url)
        self.m_domain = res.group(4)
        # print(self.m_url, self.domain)
        mod_name = str(self.m_domain)# + ".py"
        # print(mod_name)
        self.m_module = __import__('%s' %(mod_name), fromlist=[mod_name])
        self.scrap = getattr(self.m_module, 'scrap')
        self.scrap_all = getattr(self.m_module, 'scrap_all')
        self.m_lastTime = datetime.datetime.today().strftime('%H:%M')
        # self.scrap_all(url)
    def scrapAllNews(self):
        return self.scrap_all(self.m_url)
    def scarpNews(self):
        return self.scrap()


#############################################################################################
## Main
#############################################################################################

class worker(QThread):
    def __init__(self, main):
        super().__init__()
        self.m_bRun = True
        self.m_Main = main

    def run(self):
        time.sleep(30)
        while self.m_bRun:
            self.m_Main.newsScrap()
            time.sleep(60)
            print("Worker call!!")
        print("loop end!")

## Form
form_class = uic.loadUiType("D:\\30_STUDY\\python\\BeautifulSoup\\Ghong.ui")[0]
class WindowClass(QMainWindow, form_class):
# Default Function
    def __init__(self):
        #  default
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("근홍인 부자가될꺼야")
        self.timeLabel.setText(datetime.datetime.today().strftime('%m월%d일  %H:%M'))
        #self.m_tmp = 0
        #self.newListTest()
        self.teleBotInit()
        self.loadKeywords()
        self.newsScrapInit()
        self.newListInit()

        self.workerThread = worker(self)
        self.workerThread.start()

    def closeEvent(self, event):
        self.workerThread.m_bRun = False

# News Function
    def newsScrapInit(self):
        ## Read files
        self.Site_list = []
        self.News_list = []
        with open("D:\\30_STUDY\\python\\BeautifulSoup\\site\\sites.txt", "r", encoding="utf8") as data:    
            '''
            # site.txt 에 있는 목록 전부 긁어오는건데 아직 작업이 안끝났엉.
            while True:
                line = data.readline()
                if not line:
                    break
                if line[0] != '#':
                    site_list.append(site(line))
            '''
            for i in range(0,2):
                line = data.readline()
                if line != None and line[0] != '#': 
                    newSite = site(line)
                    self.Site_list.append(newSite)

            for s in self.Site_list:
                for news in s.scrapAllNews():
                    self.News_list.append(news)
        self.News_list.sort(key = lambda news : news.m_time, reverse = True)

    def newsScrap(self):
        currtime = datetime.datetime.today()
        self.timeLabel.setText(currtime.strftime('%m월%d일  %H:%M'))
        for site in self.Site_list:
            print(f"{site.m_domain} Start scrap!")
            for news in site.scrap(site.m_url, site.m_lastTime):
                item = QListWidgetItem()
                item.setText(f"{news.m_time}  {news.m_title}")
                item.setToolTip(news.m_url)
                if any(keyword in news.m_title for keyword in self.keywords):
                    item.setForeground( QColor('#ff0000') )
                    self.SendBotMsg(news)
                self.newsListWidget.insertItem(0, item)
                site.m_lastTime = news.m_time
            print(f"{site.m_domain} End scrap! time : {site.m_lastTime}")

    def newListInit(self):
        self.newsListWidget.clear()
        for news in self.News_list:
            item = QListWidgetItem()
            item.setText(f"{news.m_time}  {news.m_title}")
            item.setToolTip(news.m_url)
            if any(keyword in news.m_title for keyword in self.keywords):
                item.setForeground( QColor('#ff0000') )
                self.SendBotMsg(news)
            self.newsListWidget.addItem(item)

    def loadKeywords(self):
        self.keywords = []
        with open("keyword.txt", "r", encoding="utf8") as data:
            while True:
                line = data.readline().rstrip()
                if not line:
                    break
                self.keywords.append(line)
        print(self.keywords)

    def newListTest(self):
        #self.newsListWidget.clear()
        self.timeLabel.setText(datetime.datetime.today().strftime('%m월%d일  %H:%M'))
        item = QListWidgetItem()
        self.m_tmp += 1
        item.setText(f"{self.m_tmp} 번째.")
        self.newsListWidget.insertItem(0,item)
        #self.newsListWidget.additem("dd")

    def teleBotInit(self):
        telgm_token = "1732041372:AAFT6Mq2o0QGfcKR-RaI2YKswT6CMW-rm94"
        self.bot = telegram.Bot(token = telgm_token)
    
    def SendBotMsg(self, news):
        msg = f"[{news.m_time}] {news.m_title} \n{news.m_url}"
        self.bot.sendMessage(chat_id='807345369', text=msg)

    def slot_OpenURL(self, item):
        webbrowser.open_new(item.toolTip())

## Main 
app = QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
print('init')
print(datetime.datetime.today().strftime('%m월 %d일.  %H:%M'))
app.exec_()


print("end")