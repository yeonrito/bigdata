import requests as req
from bs4 import BeautifulSoup

url= "https://search.naver.com/search.naver?query="
query=input("검색할 내용을 입력해주세요.in>>>")
html = req.get(url+query)

data = BeautifulSoup(html.text)
ul = data.find("ul",{"class" : "_related_keyword_ul"})

final = ul.find_all("a")
for i in final:
    print(i.text)






