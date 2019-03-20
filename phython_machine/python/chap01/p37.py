'''
Created on 2018. 7. 17.

@author: big2-00
'''

from bs4 import BeautifulSoup

if __name__ == '__main__':
    fp=open("books.html",encoding='utf-8')
    soup=BeautifulSoup(fp,'html.parser')
    
    sel =  lambda q : print(soup.select_one(q).string)
    
    sel('#nu')
    sel('li#nu')
    sel('ul > li#nu')
    sel('#bible #nu')
    sel('#bible > #nu')
    sel('ul#bible > li#nu')
    sel('li[id="nu"]')
    sel("li:nth-of-type(4)")
    
    print(soup.select("li")[3].string)
    print(soup.find_all('li')[3].string)