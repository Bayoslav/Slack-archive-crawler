import requests
n=0
while(1):
    n=n+1
    r = requests.get('https://chicago.craigslist.org/search/cto?query=ford+mustang')
    content = (r.content.decode("utf-8"))          
    if (content.find('This IP has been') == 0):
        print ("BLOCKED")
        print ("NUM : ", n)
        break
