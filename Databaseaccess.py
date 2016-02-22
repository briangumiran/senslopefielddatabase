#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")


#create table
sql ="""CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)"""

cursor.execute(sql)

sel = """SELECT * FROM EMPLOYEE"""

cursor.execute(sel)
row = cursor.fetchone()
while row is not None:
  print(row)
  row = cursor.fetchone()


# disconnect from server
db.close()
