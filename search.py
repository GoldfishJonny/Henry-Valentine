import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/GoldfishJonny/Henry-Valentine')

soup = BeautifulSoup(r.content, 'html.parser')
print(r.url)
print(soup.prettify())