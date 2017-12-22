import requests
import json

position = 0
skip = 0
count = 0
numreq = 1
poslist = []
skiplist = []
while(1):

    position += count
    skip += count
    poslist.append(position)
    skiplist.append(skip)
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
        print("Ima ", numreq, "stranice")
        print("POST parametri:\n" + "position: ", (poslist),"\nskiplist:", skiplist)
        break
    numreq += 1
    #print(cont)
    #print(rows)
    count = (cont.get('Count'))
    print(count)







    #print(unicoded)
