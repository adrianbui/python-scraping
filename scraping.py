import requests
from bs4 import BeautifulSoup
import pandas as pd

website = str(input("Enter the url: "))  #input the URL
url = requests.get(website) #get HTML file from the website
soup = BeautifulSoup(url.content, "html.parser")

table = soup.find_all('table')[1]
rowsInTable = table.find_all('tr')
itemsInRow = list()


#loop through the rows in table
for tableRow in rowsInTable: 
    tableData = tableRow.find_all('td')
    row = [i.text for i in tableData]
    itemsInRow.append(row)

#Enter titles for columns
firstTitle = input("Enter the first title: ")
secondTitle = input("Enter the second title: ")
thirdTitle = input("Enter the third title: ")

dataF = pd.DataFrame(itemsInRow, columns=[firstTitle, secondTitle, thirdTitle])
dataF.set_index(firstTitle, inplace=True)
dataF.set_index(secondTitle, inplace=True)
dataF.set_index(thirdTitle, inplace=True)


#Convert data to csv file
fileName = input("Enter the filename: ")
dataF.to_csv('{}.csv'.format(fileName))
