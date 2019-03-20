'''
Created on 2018. 7. 17.

@author: big2-00
'''
from bs4 import BeautifulSoup
import urllib.request as req

if __name__ == '__main__':
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    
    res=req.urlopen(url)
    
    soup=BeautifulSoup(res,"html.parser")
    
    title=soup.find("title").string
    wf=soup.find("wf").string
    print(title)
    print(wf)    