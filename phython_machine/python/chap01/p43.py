'''
Created on 2018. 7. 17.

@author: big2-00
'''

from urllib.parse import urljoin

if __name__ == '__main__':
    base = "http://example.com/html/a.html"
    
    print(urljoin(base, "b.html"))
    print(urljoin(base, "sub/c.html"))
    print(urljoin(base, "../index.html"))
    print(urljoin(base, "../img/hoge.png"))
    print(urljoin(base,"../css/hoge.css"))