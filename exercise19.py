import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

for paragraph in soup.find_all('p'):
    paragraphType = paragraph.parent.get('class')
    if str(type(paragraphType)) == "<class 'str'>":
        if paragraphType == 'content-section':
            print(paragraph.text.strip())
    if str(type(paragraphType)) == "<class 'list'>":
        if 'content-section' in paragraphType:
            print(paragraph.text.strip())
