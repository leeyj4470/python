'''
Created on 2018. 7. 17.

@author: big2-00
'''

from bs4 import BeautifulSoup
import urllib.request as req

if __name__ == '__main__':
    url="http://info.finance.naver.com/marketindex"
    res=req.urlopen(url)
    
    soup=BeautifulSoup(res,"html.parser")
    
    price=soup.select_one("div.head_info > span.value").string
    print("usd/krw =",price)
    