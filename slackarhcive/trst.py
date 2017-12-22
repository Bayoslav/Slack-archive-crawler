import requests
import json
headers = {
  'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
  'authority' : 'api.slackarchive.io',
  'Remote-Adress' : '51.15.69.64:443',
  'referer' : 'https://productmanagerhq.slackarchive.io/ama/page-9',
  'x-alt-referer' : 'https://productmanagerhq.slackarchive.io'

}
#r = requests.get('https://api.slackarchive.io/v1/messages?size=502&team=T09C8HPAQ&channel=C0DV0F5ME', headers=headers)
#r = requests.get('https://api.slackarchive.io/v1/users?team=T09C8HPAQ&userid=U12BD6Y9F', headers=headers)
r = requests.get('https://api.slackarchive.io/v1/channels?team=T03PSJ0M8', headers=headers)
print(r.content)
lista = []
f = open('channelssec.txt', 'w')
#a = f.read()
kek = (json.loads(r.content))
dudu = kek.get('channels')
for listic in dudu:
    name = (listic.get('name'))
    idd = listic.get('channel_id')
    wrt = "{'id' :" + "'" + idd + "'" + ",'name' :" + "'" + name + "'" "}"
    lista.append(wrt)
print(lista)
f.write(str(lista))
#dudu = (kek.get('users'))
#user = dudu.find(user_id='U12BD6Y9F')

#print(r.content)
f.close()
