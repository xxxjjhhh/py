import requests

req = requests.get("https://www.youtube.com/")
//정상 -> 200 return

context = req.text

print(context)
