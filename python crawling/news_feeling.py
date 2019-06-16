import requests as req
from bs4 import BeautifulSoup
 
def get_comments(url):
     html = req.get(url)
     bs = BeautifulSoup(html.text,"html.parser")
     ul = bs.find("ul",{"class" : "u_cbox_list"})
     span = bs.find_all("span")

def check(html_text):
    f = open("test.html", "w")
    f.write(html_text)
    f.close()
     
     
if __name__ == "__main__":
    url="https://news.naver.com/main/read.nhn?m_view=1&Dsid2=264&oid=028&aid=0002454315"
    html = req.get(url)
    check(html.text)
