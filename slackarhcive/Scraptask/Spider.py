import requests
import bs4 as bs
url = 'http://www.urbanhome.ch/suchen/2499910-4-5-zimmer-wohnung'
r = requests.get(url)
soup = bs.BeautifulSoup(r.text,'lxml')
#print(soup)
#<span class="db" itemprop="streetAddress">Aeckerwiesenstrasse 24</span>
for title in soup.find_all('small',class_='cb'):
    print(title.text)

adress = soup.find('span', class_='db', attrs={'itemprop':'address'})
street = adress.find('span',class_='db',attrs={'itemprop':'streetAddress'})
print(street.text)
postalcode = adress.find('span',attrs={'itemprop':'postalCode'})
print(postalcode.text)


print("KEK")
#http://www.urbanhome.ch/Search/DoSearch - ROWS!
