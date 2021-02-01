import requests

url = "https://requests.readthedocs.io/en/master/"
res = requests.get(url)

if res.status_code == 200:
    html = res.text
    print(html)
else: print(res.status_code)