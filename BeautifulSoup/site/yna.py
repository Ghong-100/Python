from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from datetime import datetime

class news:
    def __init__(self):
        self.m_title = ''       # [속보]김근홍 휴가쓰고싶어해. "연휴가 너무 짧다"
        self.m_time = ''        # %m-%d %H:%M
        self.m_url = ''        # https://new.ghong.co.kr/latest?12345467
    def print(self):
        print(f"Time : {self.m_time}\nTitle : {self.m_title}\nURL : {self.m_url}")

def check():
    print(__name__)

def scrap(url, lastTime):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")

    newsList = []
    currTime = datetime.now().strftime('%H:%M')

    bsFind = bsObject.find('section')#, attrs={'class':'tit-news'})
    findData = bsFind.find_all(True, {"class": ["txt-time","tit-wrap","tit-news"]})
    count = 0   # 필요한 데이터가 3줄로 출력된다.
    index = 0   # 1 = 시간, 2 = url, 3 = 뉴스제목
                # 시간 확인해서 필요없으면 2번째, 3번째 줄도 스킵해줘야한다.
    skip = False
    print(f"{currTime} start parsing!!")
    for line in findData:
        index = index + 1 if index + 1 <= 3 else 1
        if index == 1:  # 시간 처리
            newsTime = str(line.get_text())[-5:]
            #newsTime = datetime.now().strftime('%Y') + '-' + newsTime
            print(newsTime, end=' ')
            if newsTime != None and newsTime >= lastTime:
                newNews = news()
                newNews.m_time = newsTime
                newsList.append(newNews)
                count += 1
                skip = False
            else:
                skip = True
        elif index == 2: # url 처리
            if skip == True:
                continue
            if 'href' in line.attrs:
                newsList[count-1].m_url = "https:" + str(line.attrs['href'])
        elif index == 3: # 뉴스 제목
            if skip == True:
                continue
            newsTitle = str(line.get_text())
            if newsTitle != None:
                newsList[count-1].m_title = newsTitle
                newsList[count-1].print()
    print(f"\n{currTime} end parsing!!", end='\n\n')
    return newsList

def scrap_all(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    newsList = []

    bsFind = bsObject.find('section')
    findData = bsFind.find_all(True, {"class": ["txt-time","tit-wrap","tit-news"]})
    count = 0
    index = 0   # 1 = 시간, 2 = url, 3 = 뉴스제목
    skip = False
    for line in findData:
        index = index + 1 if index + 1 <= 3 else 1
        if index == 1:  # 시간 처리. 뉴스 화면에 월,일이 표시되니까 걍 시간만 뽑자
            newsTime = str(line.get_text())[-5:]
            #newsTime = datetime.now().strftime('%Y') + '-' + newsTime
            if newsTime != None:
                newNews = news()
                newNews.m_time = newsTime
                newsList.append(newNews)
                count += 1
                skip = False
            else:
                skip = True
        elif index == 2: # url 처리
            if skip == True:
                continue
            if 'href' in line.attrs:
                newsList[count-1].m_url = "https:" + str(line.attrs['href'])
        elif index == 3: # 뉴스 제목
            if skip == True:
                continue
            newsTitle = str(line.get_text())
            if newsTitle != None:
                newsList[count-1].m_title = newsTitle
                newsList[count-1].print()
    return newsList

def scrap_all2(url):
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    newsList = []

    with open("BeautifulSoup\\Site\\yna_find.html","w", encoding="utf8") as output:
        bsFind = bsObject.find('section')
        findData = bsFind.find_all(True, {"class": ["txt-time","tit-wrap","tit-news"]})
        count = 0
        index = 0   # 1 = 시간, 2 = url, 3 = 뉴스제목
        skip = False
        for line in findData:
            index = index + 1 if index + 1 <= 3 else 1
            if index == 1:  # 시간 처리. 뉴스 화면에 월,일이 표시되니까 걍 시간만 뽑자
                newsTime = str(line.get_text())[-5:]
                #newsTime = datetime.now().strftime('%Y') + '-' + newsTime
                if newsTime != None:
                    newNews = news()
                    newNews.m_time = newsTime
                    newsList.append(newNews)
                    count += 1
                    skip = False
                else:
                    skip = True
            elif index == 2: # url 처리
                if skip == True:
                    continue
                if 'href' in line.attrs:
                    newsList[count-1].m_url = "https:" + str(line.attrs['href'])
            elif index == 3: # 뉴스 제목
                if skip == True:
                    continue
                newsTitle = str(line.get_text())
                if newsTitle != None:
                    newsList[count-1].m_title = newsTitle
                    newsList[count-1].print()
                    output.write(newsList[count-1].m_time + '\n')
                    output.write(newsList[count-1].m_title + '\n')
                    output.write(newsList[count-1].m_url + '\n\n')
        return newsList





'''
            if 'href' in line.attrs:
                writedata = str(line.attrs['href'])
                output.write(writedata+'\n')
            else:
                writedata = str(line.get_text())
                output.write(writedata+'\n')
'''

        # while True:
        #     findData = bsFind.find('span', attrs={'class':'txt-time'})
        #     if findData == None:
        #         break
        

        #bsFind = bsObject.find('strong', {'class':'tit-news'}).get_text()
        #output.write(str(bsObject))

        # class="tit-news"
        # class="txt-time"