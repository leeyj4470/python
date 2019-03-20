'''
Created on 2018. 7. 17.

@author: big2-00
'''
import urllib.request



if __name__ == '__main__':
    url= "http://uta.pw/shodou/img/28/214.png"
    savename="test.png"
    
    urllib.request.urlretrieve(url, savename)
    print("저장되었습니다.")