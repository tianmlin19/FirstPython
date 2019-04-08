import urllib.request

request = urllib.request.Request('http://www.baidu.com')
response = urllib.request.urlopen(request)
buff = response.read()
html = buff.decode("utf8")
print(html)