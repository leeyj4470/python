'''
Created on 2018. 4. 23.

@author: big-09
'''
from itertools import count
import urllib.request as req
import urllib 
from bs4 import BeautifulSoup

import pandas as pd

def get_soupData(page_index,enc='utf-8'):
    url="https://nenechicken.com/17_new/sub_shop01.asp?page=%s&ex_select=1&ex_select2=&IndexSword=&GUBUN=C" % str(page_idx+1)
    
    response=req.urlopen(url)    
            
    if response.getcode() == 200:
        try:
            rcv = response.read()
            ret = rcv.decode(enc)
        except UnicodeDecodeError:
            ret = rcv.decode(enc,'replace')
        
    return BeautifulSoup(ret,'html.parser')

if __name__ == '__main__':
    
    
    result=[]  
    
    for page_idx in count(): 
        
        soupData=get_soupData(page_idx,"utf-8")
        
        print("[Nene page] : [%s]" % (str(page_idx+1)))
        
        tag_div_shops = soupData.findAll('div',attrs={'class':'shop'})
        
        bEnd = True
        for tag_div_shop in tag_div_shops:
            
            bEnd = False
            
            tag_table = tag_div_shop.find('table',attrs={'class':'shopTable'})
                    
            tag_tr=tag_table.find('tr')
            
            tr_text = list(tag_tr.strings)
            
            #name=tr_text[6]
            #address=tr_text[8]
            #phone=tr_text[16]
            #sido_gu=address.split()[:2]
            
            name=tag_tr.find('div',attrs={'class':'shopName'}).text
            address=tag_tr.find('div',attrs={'class':'shopAdd'}).text
            phone=tag_tr.find('div',attrs={'class':'shopCall'}).a['href'].replace("tel:","")
            sido_gu=address.split()[:2]
            
            result.append([name]+sido_gu+[address]+[phone])      
            
        if (bEnd==True or (page_idx+1) >= 50):
            break    
            
            
    nene_table = pd.DataFrame(result,columns=('매장명','시/도','군/구','주소','전화번호'))
    nene_table.to_csv("d:/temp/chicken_data/nene_address.csv",
                      encoding='cp949',mode="w",index=False)
    print('[nene page] saved completed')    
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    