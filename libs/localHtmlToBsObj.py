from bs4 import BeautifulSoup

def localHtmlToBsObj(path):
    file = open(path, "r", encoding="utf-8")
    bsObj = BeautifulSoup(file, "html.parser")
    return bsObj