import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Shakthi#1399", database="shakthidb")

mycursor = mydb.cursor()

sql = "DELETE FROM school WHERE mark=75"

mycursor.execute(sql)

mydb.commit()
