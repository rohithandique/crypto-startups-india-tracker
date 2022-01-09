#importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

#setting the page url
URL = "https://inc42.com/the-indian-crypto-blockchain-tracker/"
page = requests.get(URL) #fetching the page content

#create a bs4 object of the page
soup = BeautifulSoup(page.text, "html.parser")

#creating an empty dataframe with required column names
df = pd.DataFrame(columns = ['Company Name', 'Website', 'Sector', 'Headquarters', 'Team Size', 'Founding Year'])

#finds listed 150 companies
for i in range(0, 150):
    #finds each specific table row element
    results = soup.find("tr", id="table_2_row_"+str(i))
    #replaces new line with '$'
    results = results.text.replace("\n", "$")
    #splits the results string into different strings
    resultArr = results.split("$")
    #saving required info in the dataframe
    df.loc[len(df.index)] = [resultArr[2], resultArr[3], resultArr[5], resultArr[6], resultArr[7], resultArr[8]]

#outputs the data to a csv file
df.to_csv('data.csv', index=False)

