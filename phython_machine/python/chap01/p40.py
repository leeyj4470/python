'''
Created on 2018. 7. 17.

@author: big2-00
'''

from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    html="""
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="https://example.com/aaa">aaa*</li>
    </ul>
    """
    
    soup=BeautifulSoup(html,'html.parser')
    
    li=soup.find_all(href=re.compile(r"^https://"))
    for e in li :
        print(e.attrs['href'])