import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysqlsifre",
    database="schooldb"

)
mycursor = connection.cursor()
mycursor.execute("Show databases")
for i in mycursor:
    print(i)