'''
Created on 2018. 8. 16.

@author: big2-01
'''
import requests


r=requests.get("http://api.aoikujira.com/time/get.php")

text=r.text
print(text)

bin=r.content
print(bin)
