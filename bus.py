import bs4
import requests
import re
from text_unidecode import unidecode

site = requests.get(
    "https://moovitapp.com/index/en/public_transit-lines-Ottawa_ON-422-2194")
soup = bs4.BeautifulSoup(site.text, 'html.parser')
# Downloading main page and finding links
links2 = soup.select('div[class="lines-container agency-lines"] a[href]')
while(True):
    select = input("Enter bus number (q to quit): ")
    if(select.upper() == "Q"):
        break
    web = ""
    bus = re.compile(r'\d+')
    for i in range(0, len(links2)):
        # Finding link with bus number
        if(bus.search(links2[i].get('href')).group() == select):
            web = links2[i].get('href')
    if(web == ""):
        print("Bus not found")
        continue
    site = requests.get("https://moovitapp.com/index/en/"+web)
    # Downloading page with bus stops
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    links = soup.select('ul[class="stops-list bordered"] h3')
    stops = []
    e = 1

    stop = input("Enter start: ")
    for i in range(0, len(links)):
        if(stop.upper() in unidecode(links[i].getText()).upper()):
            print(e, links[i].getText())
            stops.append(i)
            e += 1
    if(e == 1):
        print("Stop not found")
        continue
    one = stops[int(input("Enter number: "))-1]

    e = 1
    stops = []
    stop = input("Enter destination: ")
    for i in range(0, len(links)):
        if(stop.upper() in unidecode(links[i].getText()).upper()):
            print(e, links[i].getText())
            stops.append(i)
            e += 1
    if (e == 1):
        print("Stop not found")
        continue

    two = stops[int(input("Enter number: "))-1]
    print("There are "+str(abs(one-two)-1)+" stops")
print("Bye!")
