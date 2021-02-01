import requests

url = "https://requests.readthedocs.io/en/master/"
res = requests.get(url)

print("RESPONSE :", res)
print("METHOD OF RESPONSE :", dir(res))
print("HTML :", res.text)
print("STATUS :", res.status_code)