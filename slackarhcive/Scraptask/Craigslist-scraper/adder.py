import requests
import bs4 as bs
def getproxy():
    try:
        r = requests.get('http://api.proxyrotator.com/?apiKey=xPEjwuFkAhRrX2v43ZgVzcMWpQ9Gfs8H')
    except:
        try:
            r = requests.get('http://api.proxyrotator.com/?apiKey=xPEjwuFkAhRrX2v43ZgVzcMWpQ9Gfs8H')
        except:
            r = requests.get('http://api.proxyrotator.com/?apiKey=xPEjwuFkAhRrX2v43ZgVzcMWpQ9Gfs8H')
    dt = r.json()
    kip = str(dt.get('proxy'))
    #kip = '85.26.146.169:80'
    ip = 'http://' + kip
    httpsprox = 'https://' + kip
    proxies = {
        "http" : ip,
        "https" : httpsprox,
        #"https" : httpsprox,
        #'https' : httpsprox,
    }
    #print(ip)
    return proxies
proxies=getproxy()
url = 'https://chicago.craigslist.org/search/cto?query=ford+mustang'
ded = "6272554861"
source = requests.get(url,timeout=20,proxies = proxies)
soup = bs.BeautifulSoup(source.text, 'lxml')
#print(soup)
bab = soup.find(attrs={"data-pid" : int(ded)})
babic = soup.find('a',attrs={"data-id" : int(ded)} )
title = babic.text
href = babic['href']
#print(bab)
price = bab.find('span', class_='result-price').text
print(price)
print(title)
print(href)
