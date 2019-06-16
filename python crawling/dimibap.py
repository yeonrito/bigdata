import requests as req
from bs4 import BeautifulSoup

query=input("교장을 알고 싶나... 그럼 입력해라...")
url = "https://ko.wikipedia.org/wiki/"

html = req.get(url + query)
bs = BeautifulSoup(html.text)
table = bs.find("table", {"class" : "infobox"})
trs = table.find_all("tr")
for tr in trs:
    if "교장" in str(tr):
        td = tr.find("td")
        print(td.text)