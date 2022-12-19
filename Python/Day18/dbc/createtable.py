import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Shakthi#1399", database="shakthidb")

mycursor = mydb.cursor()

#mycursor.execute("Create table school(student_name varchar(30), mark int(20))")

mycursor.execute("Show tables")

for i in mycursor:
    print(i)