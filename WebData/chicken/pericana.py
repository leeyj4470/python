'''
Created on 2018. 4. 23.

@author: big-09
'''

from itertools import count
import urllib.request as req
 
from bs4 import BeautifulSoup

import pandas as pd


if __name__ == '__main__':
    
    result=[]
    
    print("페리카나 매장 정보 검색")
    print("\n")
    
    print("검색할 시/도 명을 입력하세요.(enter:생략)")
    si=input()
    
    print("검색할 구/군 명을 입력하세요.(enter:생략)")
    gu=input()
    
    print("검색할 매장명을 입력하세요.(enter:생략)")
    branch_name=input()
    
    for page_idx in count():
       
        url="http://pelicana.co.kr/store/stroe_search.html?page={page}&branch_name={branch_name}&gu={gu}&si={si}".format(page=str(page_idx+1),
                                                                                                                         branch_name=req.quote(branch_name.encode('utf-8'),'/:'),
                                                                                                                         gu=req.quote(gu.encode('utf-8'),'/:'),
                                                                                                                         si=req.quote(si.encode('utf-8'),'/:')
                                                                                                                         )

        html=req.urlopen(url)
        html=html.read().decode("utf-8","replace")
        
        print("[Pericana Page] : [%s]" % (str(page_idx+1)))
        
        soupData =  BeautifulSoup(html,'html.parser')
        store_address=soupData.find('table',attrs={'class':'table mt20'})
        tbody=store_address.find('tbody')
        
        bEnd=True
        for store_tr in tbody.findAll('tr'):
            bEnd=False
            tr_tag=list(store_tr.strings)            
                      
            name=tr_tag[1]
            address=tr_tag[3]
            phone=tr_tag[5].lstrip()
            sido_gu=address.split()[:2]
            
            result.append([name]+sido_gu+[address]+[phone])
            
        if (bEnd == True):
            break
        
    pericana_table = pd.DataFrame(result,columns=('매장명','시/도','군/구','주소','전화번호'))
    pericana_table.to_csv("d:/temp/chicken_data/pericana_address.csv",encoding="cp949",mode="w",index=False)
    print("[Pericana pages] saved completed")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        