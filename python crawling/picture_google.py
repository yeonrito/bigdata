import requests as req
from bs4 import BeautifulSoup
import urllib.request

def get_img(URL, NAME):
    try:
        urllib.request.urlretrieve(URL, "images/"+NAME +".png")
        print("Save " + NAME + "...")
        return True
    except:
        print("ERROR : "+NAME + "has a problem and does not save ...")
        return False

if __name__ == "__main__":
    urlfront = "https://www.google.com/search?q="
    urlend = "&tbm=isch"
    data = input("검색할 내용 입력 = ")
    
    html = req.get(urlfront + data + urlend)
    print(html.text)

    bs = BeautifulSoup(html.text)
    imgs = bs.find_all("img")
    links = []
    for img in imgs:
        links.append(img.get("src"))
    link = links[1:]
    print(links)
    cnt=0
    for link in links:
        cnt+=1
        get_img(link, "%d번 이미지" %cnt)