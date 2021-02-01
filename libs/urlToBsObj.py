import requests
from bs4 import BeautifulSoup

def urlToBsObj(url):
    res = requests.get(url)
    # url to html
    if res.status_code == 200:
        html = res.text
    else:
        print(res.status_code)
    # html to bs object
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj
