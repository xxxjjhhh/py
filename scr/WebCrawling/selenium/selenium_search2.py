import time
from selenium import webdriver

url = "https://www.naver.com"


browser = webdriver.Edge('C:\\Users\\kim\\Desktop\\vs\\msedgedriver.exe')
browser.get(url)

time.sleep(3) #browser.implicitly_wait(3)


target = browser.find_element_by_id('query')
target.send_keys("진주")
target.send_keys("\n")

browser.close()
