'''
Created on 2018. 8. 17.

@author: big2-01
'''
from selenium import webdriver

browser=webdriver.Chrome("C:\\Users\\big2-01\\Downloads\\chromedriver")
browser.implicitly_wait(3)


browser.get("https://www.google.com")

r=browser.execute_script("return 100+50")
print(r)

browser.quit()