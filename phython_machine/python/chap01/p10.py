'''
Created on 2018. 7. 17.

@author: big2-00
'''
import urllib.request

if __name__ == '__main__':
    url="http://api.aoikujira.com/ip/ini"
    res=urllib.request.urlopen(url)
    data=res.read();
    
    text=data.decode("utf-8")
    print(text)