from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>

<head>
    <title>bs4.BeautifulSoup & requests</title>
</head>

<body>
    <ul>
        <li>bs4.BeautifulSoup</li>
        <li>requests</li>
    </ul>
    <div>
        <ul>
            <li class="from">bs4</li>
            <li id="import">BeautifulSoup</li>
            <li>find</li>
            <li>select</li>
        </ul>
    </div>
    <div>
        <ul>
            <a id="import" href="https://requests.readthedocs.io/en/master/">requests</a>
        </ul>
    </div>
</body>

</html>
"""

bsObj = BeautifulSoup(html, "html.parser")
print("HTML STRING -> BS OBJECT :", bsObj)

print("FIND SPECIFIC TAG(FIRST ONE) :", bsObj.find("li"))
print("SELECT SPECIFIC TAG(FIRST ONE) :", bsObj.select_one("li"))
print(bsObj.find("li") == bsObj.select_one("li"))

print("FIND SPECIFIC TAG(ALL) :", bsObj.find_all("li"))
print("SELECT SPECIFIC TAG(ALL) :", bsObj.select("li"))
print(bsObj.find_all("li") == bsObj.select("li"))

print("FIND li IN div :", bsObj.find("div").find_all("li")) # 맨 앞 div 하나만 찾을 수 있음
print("SELECT li IN div :", bsObj.select("div>ul>li")) # 계층 구조를 만족하는 모두를 찾음
print(bsObj.find("div").find_all("li") == bsObj.select("div>ul>li")) # False

print("FIND SPECIFIC CLASS(ALL) :", bsObj.find_all(class_="from"))
print("SELECT SPECIFIC CLASS(ALL) :", bsObj.select(".from"))
print(bsObj.find_all(class_="from") == bsObj.select(".from"))

print("FIND SPECIFIC ID(ALL) :", bsObj.find_all(id="import"))
print("SELECT SPECIFIC ID(ALL) :", bsObj.select("#import"))
print(bsObj.find_all(id="import") == bsObj.select("#import"))


url = "https://requests.readthedocs.io/en/master/"
print("FIND SPECIFIC ATTRIBUTE(ALL) :", bsObj.find_all(href=url))
print("SELECT SPECIFIC ATTRIBUTE(ALL) :", bsObj.select(f"[href='{url}']")) # select("tag[attr='value']")
print(bsObj.find_all(href=url) == bsObj.select(f"[href='{url}']"))
