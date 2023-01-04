import mysql.connector as msql

import pandas as pd
conn = msql.connect(host='localhost', database='PTU_Colleges', user='root', password='Shakthi#1399')

sql_query = pd.read_sql_query(''' SELECT * FROM PTU_Colleges.details;''',conn)

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\shakt\Desktop\clean_data.csv', index = False)
df.to_excel('clean_data.xls')