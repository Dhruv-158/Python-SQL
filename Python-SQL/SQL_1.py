
# create a database in mysql

import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user='root',password='admin')
print(mydb.connection_id)
cursor = mydb.cursor()
cursor.execute("CREATE DATABASE db1")

# create a table in database

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mydb"
) 
cursor = mydb.cursor()
s = "CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,3))"
cursor.execute("s")

# insert a value in table

import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='admin',
  database='mydb'
)
cursor = mydb.cursor()
s = "INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
b1=(1,'python3',345.5)
cursor.execute(s,b1)
mydb.commit()
mydb.close()

# insert multiple records in table 

import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='admin',
  database='mydb'
)
cursor = mydb.cursor()
s = "INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
books=[(1,'python3',345),(2,'SQL',657)]
cursor.execute(s,books)
mydb.commit()
mydb.close()

# Extracting data from table

import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='admin',
  database='mydb'
)
cursor = mydb.cursor()
s="SELECT * from book"
cursor.execute(s)
result=cursor.fetchall()
for rec in result:
  print(rec)
  
# UPDATE TABLE RECORD  

import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='admin',
  database='mydb'
)
cursor = mydb.cursor()
s="UPDATE book SET price=price+10 WHERE price<200"
cursor.execute(s)
mydb.commit()

# DELETE record from table

import mysql.connector
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='admin',
  database='mydb'
)
cursor = mydb.cursor()
s="DELETE FROM book WHERE title='PHP'"
cursor.execute(s)
mydb.commit()