from bs4 import BeautifulSoup
import requests
import pandas
import xlwt

source = requests.get('https://ptu.ac.in/engineering-colleges/')
source.raise_for_status()
soup = BeautifulSoup(source.text, 'html.parser')
htmltable = soup.find('tbody')




def tableDataText(table):
    rows = []
    trs = table.find_all('tr')
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')]
    if headerow:
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs:
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')]) # data row
    return rows
list_table = tableDataText(htmltable)
list_table[:2]
dftable = pandas.DataFrame(list_table[0:])
dftable.columns = ['Serisl_No','College_Name','Rank','College_Type','Address','Phone_No']
dftable.head(4)
print(dftable)
dftable.to_csv(r'C:\Users\shakt\Desktop\data.csv', index = False)

dftable.to_excel('data.xls')



