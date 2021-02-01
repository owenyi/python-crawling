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

# bs4 find
print("FIND SPECIFIC TAG(FIRST ONE) :", bsObj.find("li"))
print("FIND SPECIFIC TAG(ALL) :", bsObj.find_all("li"))
print("FIND li IN div(ALL) :", bsObj.find("div").find_all("li"))
print("FIND SPECIFIC CLASS(ALL) :", bsObj.find_all(class_="from")) #class가 keyword라 언더바 붙이는 듯
print("FIND SPECIFIC ID(ALL) :", bsObj.find_all(id="import"))
print("FIND SPECIFIC ATTRIBUTE(ALL) :", bsObj.find_all(href="https://requests.readthedocs.io/en/master/"))