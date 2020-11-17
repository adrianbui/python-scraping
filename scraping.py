import requests
from bs4 import BeautifulSoup

page = requests.get("https://blog.ongig.com/diversity-and-inclusion/biased-language-examples/")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find_all())