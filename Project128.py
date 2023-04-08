from bs4 import BeautifulSoup
""" beautifulsoup is used to see the doc as html file """
import time
import requests 
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")

star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')


row_list = []
for tr in table_rows:
    td = tr.find_all('td')
    """ print(td) """
    row = [i.text.rstrip() for i in td]
    """ print(row) """
    row_list.append(row)
    """ print(row_list) """
    


star_name = []
radius = []
mass = []
distance = []
lum = []

for i in range(1,len(row_list)):
    star_name.append(row_list[i][1])
    distance.append(row_list[i][3])
    mass.append(row_list[i][5])
    radius.append(row_list[i][6])
    lum.append(row_list[i][7])
    
headers = ['Star_name','Distance','Mass','Radius','Luminosity']    
df2 = pd.DataFrame(list(zip(star_name,radius,mass,distance,lum)),columns=headers)
print(df2)

df2.to_csv('bright_stars.csv', index=True, index_label="id")

