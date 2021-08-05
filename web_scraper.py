from bs4 import BeautifulSoup
import requests
from requests import status_codes

url = "https://www.binance.com/en/about"
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

title = soup.title
# print(type(title.string))

paras = soup.find_all('p')
# print(paras)
anchors = soup.find_all('a')
# print(anchors)

# print(soup.find('p')['class'])

# print(soup.find('a')['class'])

# print(soup.find('a')['id'])

#print(soup.find_all('a', class_='css-1mvf8us'))

# print(soup.find('a').get_text)
# print(soup.get_text)
all_links = set()

for link in anchors:
    if(link.get('href') != '#'):
        all_links.add(link.get('href'))
        print(all_links, end="\n")
