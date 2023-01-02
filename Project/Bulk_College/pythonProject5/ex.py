import mysql.connector as msql

import pandas.io.sql as sql
conn = msql.connect(host='localhost', database='Bulk_College', user='root', password='Shakthi#1399')

df=sql.read_sql('select * from details', conn)
print(df)
df.to_excel('Bulk_College.xls')