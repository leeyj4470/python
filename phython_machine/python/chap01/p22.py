'''
Created on 2018. 7. 17.

@author: big2-00
'''
from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup=BeautifulSoup(
        "<p><a href='a.html'>test</a></p>",
        "html.parser")
    
    print(soup.prettify())
    
    a=soup.p.a
    
    print(type(a.attrs))
    
    print('href' in a.attrs)
    
    print(a['href'])
    
    
    
    
    
    
    
    
