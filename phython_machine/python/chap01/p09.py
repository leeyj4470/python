'''
Created on 2018. 7. 17.

@author: big2-00
'''

import urllib.request


if __name__ == '__main__':
    url= "http://uta.pw/shodou/img/28/214.png"
    savename="test.png"
    
    mem=urllib.request.urlopen(url).read()
    
    with open(savename,mode="wb") as f:
        f.write(mem)
        print("저장되었습니다.")