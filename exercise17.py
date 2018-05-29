import requests
from bs4 import BeautifulSoup
import re

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

for stories in soup.find_all(re.compile('^h\d')):
    headingClass = stories.get('class')
    if str(type(headingClass)) == "<class 'str'>":
        if headingClass == 'story-heading':
            print(stories.text.strip())
    if str(type(headingClass)) == "<class 'list'>":
        if 'story-heading' in headingClass:
            print(stories.text.strip())    
