import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Shakthi#1399")

print(mydb)

if(mydb):
    print('success')

else:
    print('fail')
