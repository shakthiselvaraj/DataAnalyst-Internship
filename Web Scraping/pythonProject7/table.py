import pandas as pd
a = pd.read_csv("C:\\Users\\shakt\\Desktop\\data.csv", index_col=False, delimiter = ',')
a.head()



a = a.where((pd.notnull(a)), None)



import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', database='PTU_Colleges', user='root', password='Shakthi#1399')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS details;')
        print('Creating table....')
        cursor.execute("CREATE TABLE details(Serial_No int,College_Names varchar(255),Seats varchar(255),College_Type varchar(255),Address varchar(255),Phone_No varchar(255))")
        print("Table is created....")
        for i,row in a.iterrows():
            sql = "INSERT INTO PTU_Colleges.details VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)