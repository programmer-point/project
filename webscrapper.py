#this will scrap all the links 

import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

#provide the url of website
fhand=urllib.request.urlopen('https://www.amazon.in/')
#it will fix the broken html
soup=BeautifulSoup(fhand,'html.parser')
print(soup)
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))
