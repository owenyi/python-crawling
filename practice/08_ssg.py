from libs.urlToBsObj import urlToBsObj

url = "http://www.ssg.com/search.ssg?target=all&query=된장"
bsObj = urlToBsObj(url)

liList = bsObj.select("ul#idProductImg>li")

img = "http:" + liList[0].select_one("img")["src"]
name = liList[0].select_one("em.tx_ko").text
link = "http://www.ssg.com/" + liList[0].select_one("a")["href"]
price = liList[0].select_one("em.ssg_price").text

print(img)
print(name)
print(link)
print(price)