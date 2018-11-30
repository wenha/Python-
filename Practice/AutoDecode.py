import chardet
import urllib

detail = urllib.request.urlopen('http://www.quanshuwang.com/book/0/567').read()
print(detail)
chardit = chardet.detect(detail)

print(chardit['encoding'])