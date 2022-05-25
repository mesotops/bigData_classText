# -*- coding: utf-8 -*-   [   Code 7-2 :     ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
import requests
from bs4 import BeautifulSoup

web = requests.get("https://udn.com/news/cate/2/6638" )
content = BeautifulSoup( web.text, "html.parser" )

NewsTitles = content.select( ".story-list__text h2" )
for i in NewsTitles[3:]:
    print("標題：" + i.text[1:-1] )

