import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.naver.com/")

soup = BeautifulSoup(req.text, "html.parser")
context = soup.title 
print(context)

//soup.html.body.h1 등 hierarchy를 이용해 사용
