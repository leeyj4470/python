'''
Created on 2018. 7. 17.

@author: big2-00
'''

import urllib.request
import urllib.parse


if __name__ == '__main__':
    API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    values={
            'stnId':'108'
        }
    params=urllib.parse.urlencode(values)
    
    url=API+"?"+params
    print("url=",url)
    
    data=urllib.request.urlopen(url).read()
    text=data.decode("utf-8")
    print(text)
    