from libs.urlToBsObj import urlToBsObj

def getProducts(keyword):
    url = "http://www.ssg.com/search.ssg?target=all&query=된장"
    bsObj = urlToBsObj(url)

    liList = bsObj.select("ul#idProductImg>li")

    products = []
    for i in range(len(liList)):
        product = {
            "img": "http:" + liList[i].select_one("img")["src"],
            "name": liList[i].select_one("a>em.tx_ko").text,
            "link": "http://www.ssg.com/" + liList[i].select_one("a")["href"],
            "price": liList[i].select_one("em.ssg_price").text
        }
        products.append(product)

    print(products)

getProducts("된장")