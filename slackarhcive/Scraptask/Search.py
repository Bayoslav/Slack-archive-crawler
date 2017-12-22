import requests
import json
import bs4 as bs

#http://www.urbanhome.ch/Search/DoSearch
position = 0
skip = 0
count = 0
numreq = 1
lista=[]
f = open('jsondata.json','a')
while(1):

    position += count
    skip += count

    payload = {
      "settings": {
        "MainTypeGroup": "1",
        "Category": "1",
        "AdvancedSearchOpen": "false",
        "MailID": "",
        "PayType": "1",
        "Type": "0",
        "RoomsMin": "0",
        "RoomsMax": "0",
        "PriceMin": "0",
        "PriceMax": "0",
        "Regions": [
          "188542"
        ],
        "SubTypes": [
          "0"
        ],
        "SizeMin": "0",
        "SizeMax": "0",
        "Available": "",
        "NoAgreement": "false",
        "FloorRange": "0",
        "RentalPeriod": "0",
        "equipmentgroups": [],
        "Email": "",
        "Interval": "0",
        "SubscriptionType1": "true",
        "SubscriptionType2": "true",
        "SubscriptionType4": "true",
        "SubscriptionType8": "true",
        "SubscriptionType128": "true",
        "SubscriptionType512": "true",
        "Sort": "0"
      },
      "manual": 'false',
      "skip": skip,
      "reset": 'false',
      "position": position,
      "iframe": 0,
      "defaultTitle": 'true',
      "saveSettings": 'false'
    }
    print("Skip: " + str(skip))
    print("Pos: " + str(position))
    r=requests.post('http://www.urbanhome.ch/Search/DoSearch',json=payload)
    src = r.text
    cont = json.loads(r.content)
    print(cont.get('MaximumReached'))
    if(str(cont.get('MaximumReached'))=='True'):
        print("Pages it took: ", numreq)
        break
    numreq += 1
    #print(cont)
    rows = (cont.get('Rows'))
    #print(rows)
    count = (cont.get('Count'))
    print(count)
    #print(type(rows))
    #print(rows)
    rows=rows.encode('latin1').decode('unicode-escape')
    #print(rows)
    soup = bs.BeautifulSoup(rows,'lxml')
    #print(soup)
    i=0

    for ad in soup.find_all('div', class_='a ax'):
        i+=1
        url = (ad.find('a').get('href'))
        title =  (ad.find('a').text)
        adress = (ad.find('div', class_='a ay'))
        street = (adress.find('p',class_='pt15').text)
        pcode = (adress.find('p',class_='').text)
        equipment = []
        for equi in ad.find_all('span', class_='fl pr6'):
            equipment.append(equi.text)
        print(street)
        print(pcode)
        print("TITLE: " + title + "\nURL: " + url + "\n Adress: " + street + " " + pcode + "\nEquipment: " + str(equipment))
        equipment = [item[1:len(item)] for item in equipment]
        print(equipment)



        jsondict = {
            "name" : title,
            "address" : {
                "street": street,
                "city": "Winterthur",
        		"zipcode":8400
                },
            "additionalFeatures" : {
                "equipment" : {item : 'true' for item in equipment }
            }

        }
        print(jsondict)

        lista.append(jsondict)
        print(i)
jsonlista = json.dumps(lista)
f.write(jsonlista)
f.close()


    #print(unicoded)
