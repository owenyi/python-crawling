import requests
from bs4 import BeautifulSoup

url = "https://www.kurly.com/shop/main/index.php"

res = requests.get(url)

# url to html
if res.status_code == 200:
    html = res.text
else:
    print(res.status_code)

# html to bs object
bsObj = BeautifulSoup(html, "html.parser")

print(bsObj.select_one("span.txt"))
print(bsObj.select_one("span.txt").text)
# print(bsObj.select_one("span.txt").text) 오류

print(bsObj.select("span.txt"))
print(bsObj.select("span.txt")[0].text)