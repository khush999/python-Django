import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kjnr"
)

mycursor = mydb.cursor()
mycursor.execute()
