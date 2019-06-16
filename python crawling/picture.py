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
    url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
    data = input("검색할 내용 입력 : ")
    html = req.get(url + data)
    bs = BeautifulSoup(html.text)
    div = bs.find("div", {"class" : "photo_grid _box"})
    imgs =div.find_all("img")
    cnt=0
    for img in imgs:
        data = str(img)
        data = data.split("data-source=")
        url = data[1].split("\"")[1]
        get_img(url,str(cnt)+ "번 이미지")
        cnt += 1

    
    