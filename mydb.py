import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='arham',
    passwd='Jain@321'
)

#A cursor allows you to execute SQL queries, fetch data from the database, and manage the context of a fetch operation.
cursorObject=database.cursor()

#cursorObject.execute() is a method used to execute a single SQL statement. In this case, it executes the SQL command to create a new database named elderco.
#The cursor object communicates with the MySQL server and sends the command for execution.
cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE")