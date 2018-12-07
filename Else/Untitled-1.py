import re
import requests
from bs4 import BeautifulSoup

# response = requests.get('http://jr.jd.com')
# bs_obj = BeautifulSoup(response.text, 'html.parse')
# text_list = bs_obj.find_all("a","nav-item-primary")
# for text in text_list:
#     print(text.get_text())


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html)

print(soup.prettify())
print('这是标题')
print(soup.title)
print('这是头')
print(soup.head)
print('这是a')
print(soup.a)