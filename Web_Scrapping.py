# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:18:03 2023

@author: Krushna Lad
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(open("C:/Dataset/sample_doc.html"),'html.parser')
print(soup)
#It is going to show all the html contents extracted
soup.find("address")
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table
for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)

#It will show all the rows except first row

"""
[<td>Gangaram</td>, <td>B.Tech</td>, <td>NA</td>, 
 <td>NA</td>]
[<td>Ganga</td>, <td>B.A.</td>, <td>NA</td>, <td>NA</td>]
[<td>Ram</td>, <td>B.Tech</td>, <td>M.Tech</td>, <td>NA</td>]
[<td>Ramlal</td>, <td>B.Music</td>, <td>NA</td>, <td>Diploma in Music</td>]
"""