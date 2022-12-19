import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Shakthi#1399", database="shakthidb")

mycursor = mydb.cursor()

sql = "UPDATE school SET mark=75 WHERE student_name='sha'"

mycursor.execute(sql)
mydb.commit()