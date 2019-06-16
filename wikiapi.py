import requests as req
from bs4 import BeautifulSoup

def Main(query):
    print(query)
    url = "https://ko.wikipedia.org/wiki/"

    html = req.get(url + query)
    bs = BeautifulSoup(html.text)
    table = bs.find("table", {"class" : "infobox"})
    trs = table.find_all("tr")
    for tr in trs:
        if "교장" in str(tr):
            td = tr.find("td")
            return td.text

if __name__ == "__main__":
    url = "https://ko.wikipedia.org/wiki/경기도의_고등학교_목록"
    html = req.get(url)
    bs = BeautifulSoup(html.text)
    div = bs.find("div", {"class" : "mw-parser-output"})
    ps = div.find_all("p")
    datas = []
    for p in ps:
        a = p.find_all("a")
        datas +=a
    results = []
    for data in datas:
        results.append(data.text)

    principal = {}
    for school in results[:50]:
        try:
            re = Main(school)
            if re is not None:
                principal[school] = re.strip()
        except:
            pass
    
    print(principal)