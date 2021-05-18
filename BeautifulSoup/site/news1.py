from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from datetime import datetime
import json

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

def check():
    print(__name__)

def scrap(url, lastTime):
    newsList = []
    return newsList

def scrap_all(url):
    global lastnewslist
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    newsList = []
    count = 0

    ### 사이트별 다르게 파싱해줘야함.
    # 뉴스는 최신 뉴스가 먼저 나옴
    # print(findData["article_id"])       # https://www.news1.kr/articles/?기사ID     가 주소임
    # print(findData["title"])
    # print(findData["pubdate"][11:16])

    bsFind = json.loads( str(bsObject) )
    for findData in bsFind["data"]:
        if findData["title"] == None:
            break
        newNews = news(findData["title"], "https://www.news1.kr/articles/?" + str(findData["article_id"]), findData["pubdate"][11:16])
        newsList.append(newNews)
        count += 1

    # 지난 뉴스 리스트 올려주기
    if len(newsList) > 0:
        time = newsList[0].m_time
        for n in newsList:
            if n.m_time == time:
                lastnewslist.append(n)
            else:
                break

    for ln in lastnewslist:
        print("Last New : " + ln.m_title)

    return newsList


'''
def scrap(url, lastTime):
    global lastnews
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
    firstnew = True
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
            elif newsTime != None and len(lastnews) > 0 and newsTime < lastnews[0].m_time:  # 지난 뉴스보다 오래된 내용이면 끝
                return reversed(newsList)
            else:   # 시,분은 같은데 초단위가 다를수있음. 분단위 차이날때까지는 계속 봐줘야함.
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
                if firstnew:    # 중복 체크용 최신 뉴스 정보 보관
                    # 지난 사이클 최신 뉴스랑 비교해서 넘길지 말지 정해야함.
                    # 순서가 최신 -> 오래된거 순으로 나옴.
                    # 지난 뉴스 리스트에는 55분꺼 있고
                    # 지금 새로 뽑은거는 56분이 최신이고 56분꺼, 55분꺼 로테이션이 돌거임
                    # 지난 뉴스리스트와 55분꺼를 확인해줘야하고
                    # 새로운 뉴스리스트에 56분꺼를 넣어줘야함.

                    firstnew = False
                newsList[count-1].print()
    print(f"\n{currTime} end parsing!!", end='\n\n')

    return reversed(newsList)

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
'''