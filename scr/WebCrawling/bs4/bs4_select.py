import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

req = requests.get(url)
bs = BeautifulSoup(req.text, "html.parser")

lilist = bs.select('li.category_item>a') #using select <li class="category_item"><a href="">
for li in lilist:
    print(li)
