from libs.localHtmlToBsObj import localHtmlToBsObj

bsObj = localHtmlToBsObj("../kurly/index.html")

txts = bsObj.select("span.txt")
print(len(txts))

for i in range(len(txts)):
    print(txts[i].text)

inactiveImgs = bsObj.select("img.ico_off")
print(len(inactiveImgs))

for i in range(len(inactiveImgs)):
    print(inactiveImgs[i]["src"])

activeImgs = bsObj.select("img.ico_on")
print(len(activeImgs))

for i in range(len(activeImgs)):
    print(activeImgs[i]["src"])

ico_news = bsObj.select("span.tit")
print(len(ico_news))

for i in range(len(ico_news)):
    print(ico_news[i].select_one("span.ico_new") is not None)

uls = bsObj.select("ul.sub_menu")
print(len(uls))

namesList = [x.select("span.name") for x in uls]
print(namesList)

for i in range(len(namesList)):
    print([x.text for x in namesList[i]])

# names = [[y.text for y in x.select("span.name")] for x in uls]
# print(names)
# print(len(names))