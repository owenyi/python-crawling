from libs.urlToBsObj import urlToBsObj

url = "http://www.ssg.com/search.ssg?target=all&query=된장"
bsObj = urlToBsObj(url).select_one("ul#idProductImg")

img = "http:" + bsObj.select("img.i1")[0]["src"] # src attribute value
print(img)

name = bsObj.select("em.tx_ko")[0].text
print(name)

link = "http://www.ssg.com/" + bsObj.select("a.clickable")[0]["href"]
print(link)

price = bsObj.select("em.ssg_price")[0].text
print(price)

img = bsObj.select("img.i1")
name = bsObj.select("em.tx_ko")
link = bsObj.select("a.clickable")
price = bsObj.select("em.ssg_price")
print(len(img)) # 80
print(len(name)) # 116
print(len(link)) # 472
print(len(price)) # 84