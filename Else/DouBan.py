import requests
from bs4 import BeautifulSoup
import time
import datetime
from openpyxl import workbook

class Spider():
    url = 'http://movie.douban.com/top250/'
    name = []
    star_con = []
    score = []
    info = []
    headers = [
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
        {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
    ]

    def __init__(self):
        print('start: %s' % str(datetime.date.today())+" "+time.strftime("%H:%M:%S"))
        self.items_list()
        print('end: %s' % str(datetime.date.today())+" "+time.strftime("%H:%M:%S"))

    def items_list(self):
        while url:
            doc = get_page(url)


    def get_page(url):
        data = requests.get(url,headers=random.choice(headers)).content
        return data

    def get_content(doc):
        soup = BeautifulSoup(soup,'html.parser')
        ol = soup.find('ol',class='grid_view')