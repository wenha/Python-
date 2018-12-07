import requests

res = requests.get('http://www.qiushibaike.com/')

print(res.text)