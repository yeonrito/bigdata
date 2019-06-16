from bs4 import BeautifulSoup
import requests as req
import urllib as ul

with urllib.request.urlopen(web_url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser') html = response.read()
    s
