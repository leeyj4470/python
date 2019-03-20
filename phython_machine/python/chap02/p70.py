'''
Created on 2018. 8. 17.

@author: big2-01
'''
from selenium import webdriver
import time
import random

USER="아이디"
PASS="패스워드"

browser = webdriver.Chrome("C:/Users/big2-01/Downloads/chromedriver")
browser.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

e=browser.find_element_by_id("id")
e.click()
e.send_keys(USER)

e=browser.find_element_by_id("pw")
e.click()
e.send_keys(PASS)
  
form=browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.click()
print("로그인 버튼을 클릭합니다.")

browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")


products=browser.find_elements_by_css_selector("div.p_info span")

print(products)
for product in products:
    print("-",product.text)

browser.quit()