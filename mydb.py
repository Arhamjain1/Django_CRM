import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='arham',
    passwd='Jain@321'
)

cursorObject=database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE")