import requests
from bs4 import BeautifulSoup

website = str(input())
page = requests.get(website)
soup = BeautifulSoup(page.content, 'lxml')

print(soup)