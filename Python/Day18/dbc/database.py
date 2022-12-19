import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Shakthi#1399")

mycursor = mydb.cursor()

mycursor.execute("Create database shakthidb")

mycursor.execute("Show databases")

for i in mycursor:
    print(i)