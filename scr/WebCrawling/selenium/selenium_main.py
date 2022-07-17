import time
from selenium import webdriver

url = "https://www.naver.com"


browser = webdriver.Edge('C:\\Users\\kim\\Desktop\\vs\\msedgedriver.exe')
browser.get(url)

time.sleep(3) #browser.implicitly_wait(3)
print(browser.title)

browser.close()
