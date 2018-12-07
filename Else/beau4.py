import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.baidu.com')
response.encoding = 'utf-8'
print(response.text)

bs = BeautifulSoup(response.text, "html.parser")

for item in bs.find_all("a"):
    print(item.get_text())