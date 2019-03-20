'''
Created on 2018. 7. 17.

@author: big2-00
'''
import sys
import urllib.request as req
import urllib.parse as parse



if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("USAGE: download-forecast-argv <Region Number>")
        sys.exit()
    regionNumber=sys.argv[1]
    
    API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
    values={
            'stnId':'108'
        }
    params=parse.urlencode(values)
    
    url=API+"?"+params
    print("url=",url)
    
    data=req.urlopen(url).read()
    text=data.decode("utf-8")
    print(text)