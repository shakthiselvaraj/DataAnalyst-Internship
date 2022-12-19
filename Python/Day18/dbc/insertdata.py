import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Shakthi#1399", database="shakthidb")

mycursor = mydb.cursor()

sql = "Insert into school(student_name,mark) values(%s,%s)"

students = [('shakthi', 85), ('sha', 80)]

mycursor.executemany(sql, students)
mydb.commit()
