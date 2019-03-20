'''
Created on 2018. 7. 17.

@author: big2-00
'''

from bs4 import BeautifulSoup

if __name__ == '__main__':
    html="""
    <html><body>
        <h1>스크레핑이란?</h1>
        <p>웹 페이지를 분석하는 것</p>
        <p>원하는 부분을 추출하는 것</p>
    </bod></html>
    """
    
    soup=BeautifulSoup(html,'html.parser')
    
    h1=soup.html.body.h1
    p1=soup.html.body.p
    p2=p1.next_sibling.next_sibling
    
    print("h1 = "+h1.string)
    print("p1 = "+p1.string)
    print("p2 = "+p2.string)
    
    