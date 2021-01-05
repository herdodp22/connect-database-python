# menampilkan data di database menggunakan python
# create by herdodp
# follow my instagram : herdodp


import mysql.connector    # import module connector
import os    # import module os


# create database variable
db = mysql.connector.connect(    
    host = "localhost",
    user = "root",  # xampp default
    passwd = "",
    database = "db_careio"   # insert with your database name
)

# create tampilkan_data function
def tampilkan_data(db) :
    cursor = db.cursor()
    sql = "SELECT * FROM dataregister"   # dataregister is my database table, fill with your name table database
    cursor.execute(sql)
    result = cursor.fetchall()  # take all data in table 
    
    if cursor.rowcount < 0 :
        print("tidak ada data di database")    # if no data in table
    
    else :
        for data in result :   # if success detect data
            print(data)

# call tampilkan_data function        
tampilkan_data(db)
