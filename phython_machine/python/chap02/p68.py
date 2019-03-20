'''
Created on 2018. 8. 16.

@author: big2-01
'''
from selenium import webdriver

url="http://www.naver.com"


browser=webdriver.PhantomJS("C:/Users/big2-01/Downloads/phantomjs-2.1.1-windows/bin/phantomjs")

browser.implicitly_wait(3)

browser.get(url)

browser.save_screenshot("website.png")

browser.quit()