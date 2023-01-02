import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Shakthi#1399", database="college_details")

mycursor = mydb.cursor()

#mycursor.execute("select distinct state from details")
mycursor.execute(" select * from details order by collegename")


result = mycursor.fetchall()

for i in result:
    print(i)