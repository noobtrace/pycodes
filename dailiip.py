import urllib.request

url = 'http://www.whatismyip.com.tw'

#代理ip
proxy_support = urllib.request.ProxyHandler({'http':'202.5.38.25:8080'})

opener = urllib.request.build_opener(proxy_support)
#opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html= response.read().decode('utf-8')

print(html)
