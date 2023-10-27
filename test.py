import requests
from bs4 import BeautifulSoup
import pandas as pd

#url='https://www.scrapethissite.com/pages/'
#html=requests.get(url)
# 
#soup=BeautifulSoup(html.text,'html.parser')
#
#demo=soup.find('p',class_='lead session-desc').text
#print(demo.strip())

url='https://en.wikipedia.org/wiki/List_of_companies_of_Oman'
html=requests.get(url)

soup=BeautifulSoup(html.text,'html.parser')

demo=soup.find('tr').text
first_row = demo.strip().split()
df = pd.DataFrame(columns=first_row)

col_data=soup.find_all('tr')

for row in col_data[1:5]:
    row_data=row.find_all('td')
    ind_row_data = [data.text.strip() for data in row_data]
   
    length=len(df)
    df.loc[length] = ind_row_data

print(df)
    


    





