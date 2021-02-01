from bs4 import BeautifulSoup

html = "<div><ul><li>bs4</li><li>BeautifulSoup</li></ul></div>"
bsObj = BeautifulSoup(html, "html.parser")

print("HTML STRING -> BS OBJECT :",bsObj)
print("TYPE OF BS OBJECT :", type(bsObj))