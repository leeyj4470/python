'''
Created on 2018. 7. 17.

@author: big2-00
'''
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html="""
    <html><body>
        <ul>
            <li><a href="http://www.naver.com">naver</a></li>
            <li><a href="http://www.daum.net">daum</a></li>
        </ul>
    </body></html>
    """
    
    soup=BeautifulSoup(html, 'html.parser')
    
    links=soup.find_all("a")
    
    for a in links:
        href=a.attrs['href']
        text=a.string
        print(text,">",href)
    