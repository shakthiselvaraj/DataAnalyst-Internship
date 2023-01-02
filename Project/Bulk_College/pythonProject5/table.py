import pandas as pd
a = pd.read_csv("C:\\Users\\shakt\\Downloads\\College Data to clean and sort.xlsx - Bulk College Data.csv", index_col=False, delimiter = ',')
a.head()



a = a.where((pd.notnull(a)), None)



import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', database='Bulk_College', user='root', password='Shakthi#1399')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS details;')
        print('Creating table....')
        cursor.execute("CREATE TABLE details(id int,collegename varchar(255),state varchar(255),district varchar(255),mail varchar(255),phone varchar(255))")
        print("Table is created....")
        for i,row in a.iterrows():
            sql = "INSERT INTO Bulk_College.details VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)

