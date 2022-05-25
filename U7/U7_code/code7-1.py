# -*- coding: utf-8 -*-   [   Code 7-1 :   Web Crawler   ]  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
import requests
url = "https://udn.com/news/cate/2/6638"
html = requests.get(url).text
print (html)
