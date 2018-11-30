import requests
import re

def Page_Info(myPage):
    '''Regex'''
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
    return mypage_Info

def Spider(url):
    i = 0
    print('DownLoading',url)
    myPage = requests.get(url).content.decode('gbk')
    myPageRequests = Page_Info(myPage)

if __name__ == "__main__":
    print('Start')
    start_url = 'http://news.163.com/rank'
    Spider(start_url)
    print('End')