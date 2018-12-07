import requests
import time
import datetime
import random
import os

class Spider():
    url='http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html'
    headers = [
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
        {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
    ]
    def __init__(self):
        print('start：%s' %(str(datetime.date.today()) + ' ' + time.strftime('%H:%M:$S')))
        self.content()
        print('end: %s' % (str(datetime.date.today()) +'' + time.strftime('%H:%M:%S')))

    def content(self):
        content = requests.get(self.url, headers = random.choice(self.headers))

        f = open('blog.html','w',encoding='utf-8')
        f.write(content.text)

        f.close()


if __name__ == "__main__":
    sp = Spider()
