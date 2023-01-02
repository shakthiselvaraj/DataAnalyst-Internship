import mysql.connector as msql

import pandas as pd
conn = msql.connect(host='localhost', database='Bulk_College', user='root', password='Shakthi#1399')

sql_query = pd.read_sql_query(''' SELECT * FROM bulk_college.details;''',conn)

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\shakt\Desktop\exported_data.csv', index = False)