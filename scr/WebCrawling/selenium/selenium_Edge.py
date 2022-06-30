from selenium import webdriver

url = "https://www.naver.com"

browser = webdriver.Edge('C:\\Users\\kim\\Desktop\\vs\\msedgedriver.exe') #\할 경우 주석처리가 됨으로 escape sequence로 \\ 
req = browser.get(url)
