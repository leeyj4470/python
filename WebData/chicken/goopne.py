'''
Created on 2018. 4. 23.

@author: big-09
'''
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count

from selenium import webdriver
import time

def GoobneAddress(result):
    Goobne_URL = 'http://www.goobne.co.kr/store/search_store.jsp'
    
    wd = webdriver.Chrome('C:/webdriver/chromedriver.exe')
    wd.get(Goobne_URL)
    time.sleep(10)
    
    for page_idx in count():
        wd.execute_script("store.getList('%s')" % str(page_idx + 1))
        print ("PageIndex [%s] Called" % (str(page_idx + 1)))
    
        time.sleep(5)
        
        rcv_data = wd.page_source
        
        soupData = BeautifulSoup(rcv_data, 'html.parser')
        
        for store_list in soupData.findAll('tbody', 
                                           attrs={'id': 'store_list'}):
            for store_tr in store_list:
                
                tr_tag = list(store_tr.strings)
                
                if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                    return result 
                
                store_name = tr_tag[1]
                store_address=''
                store_phone=tr_tag[3]
                if (tr_tag[3] == ''):                    
                    store_address = tr_tag[5]
                else:
                    store_address = tr_tag[6]                    
                store_sido_gu = store_address.split()[:2]

                result.append([store_name] + store_sido_gu + 
                              [store_address]+[store_phone])
         
def main():
    
    result=[]
    
    print('GOOBNE ADDRESS CRAWLING START')
    GoobneAddress(result)
    
    goobne_table = pd.DataFrame(result, columns=('store', 'sido',
                                            'gungu', 'store_address','store_phone'))
    goobne_table.to_csv("d:/temp/chicken_data/goobne.csv",
                         encoding="cp949", mode='w', index=True)
    print("Saved goobne.csv")
    
    
if __name__ == '__main__':
    main()
    
    
    
    