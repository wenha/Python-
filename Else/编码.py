from urllib import parse
from urllib import request

url = 'http://www.baidu.com/s?'

dict1 = {'wd':'百度翻译'}
url_data = parse.urlencode(dict1)
print(url_data)

data = request.urlopen((url+url_data)).read()
data = data.decode('utf-8')
print(data)
