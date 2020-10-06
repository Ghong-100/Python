from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

def check():
    print(__name__)

def scrap(url):
    print(url + '스크랩을 시작!!')

    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    print(type(bsObject))

    with open("BeautifulSoup\\Site\\yna_find.html","w", encoding="utf8") as output:
        bsFind = bsObject.find('section')#, attrs={'class':'tit-news'})
        print(type(bsFind))
        findData = bsFind.find_all(True, {"class": ["txt-time","tit-wrap","tit-news"]})
        #bsFind = bsFind.find_all(True, {"class": ["txt-time","tit-news"]})
        for line in findData:
            if 'href' in line.attrs:
                writedata = str(line.attrs['href'])
                output.write(writedata+'\n')
            else:
                writedata = str(line.get_text())
                output.write(writedata+'\n')
            print("One line end!!!!")
        # while True:
        #     findData = bsFind.find('span', attrs={'class':'txt-time'})
        #     if findData == None:
        #         break
        

        #bsFind = bsObject.find('strong', {'class':'tit-news'}).get_text()
        #output.write(str(bsObject))

        # class="tit-news"
        # class="txt-time"