import requests
from bs4 import BeautifulSoup
import pandas as pd

website = str(input("Enter the url: "))  #input the URL
url = requests.get(website) #get HTML file from the website
soup = BeautifulSoup(url.content, "html.parser")

table = soup.find_all('table')[1]
rowsInTable = table.find_all('tr')
itemsInRow = list()

for tableRow in rowsInTable: #loop through the rows in table
    tableData = tableRow.find_all('td')
    row = [i.text for i in tableData]
    itemsInRow.append(row)


firstTitle = input("Enter the first title: ")
secondTitle = input("Enter the second title: ")
thirdTitle = input("Enter the third title: ")

dataF = pd.DataFrame(itemsInRow, columns=[firstTitle, secondTitle, thirdTitle])
dataF.set_index(secondTitle, inplace=True)

fileName = input("Enter the filename: ")
dataF.to_csv('{}.csv'.format(fileName))
