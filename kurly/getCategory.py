from libs.localHtmlToBsObj import localHtmlToBsObj

bsObj = localHtmlToBsObj("./index.html")


inactiveImgs = bsObj.select("img.ico_off")

activeImgs = bsObj.select("img.ico_on")

txts = bsObj.select("span.txt")

ico_news = bsObj.select("span.tit")

uls = bsObj.select("ul.sub_menu")
namesList = [x.select("span.name") for x in uls]

menus = []
for i in range(len(txts)):
    menu = {
        "inactiveImgs": inactiveImgs[i]["src"],
        "activeImgs": activeImgs[i]["src"],
        "txt": txts[i].text,
        "ico_new": ico_news[i].select_one("span.ico_new") is not None,
        "names": [x.text for x in namesList[i]]
    }
    menus.append(menu)
print(menus)