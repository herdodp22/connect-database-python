# connect database using python and input data sampling
# tutorial create by herdodp
# follow my instagram : herdodp


import mysql.connector   # import module connector
import os      # import ose

db = mysql.connector.connect(    
    host = 'localhost',  # host 
    user = 'root',   # user  ( xampp )
    password = '',  # password
    database = 'db_careio' # database name ( fill with your database name)
)

def insert_data(db):   # function insert_data
    nama_user = input("Masukan nama: ")          # input name
    password_user = input("Masukan password: ")   # input pass
    val = (nama_user, password_user)   
    cursor = db.cursor()
    sql = "INSERT INTO dataregister (nama_user, password_user) VALUES (%s, %s)"    # SQL query for insert data to table database
    cursor.execute(sql, val)      # execute sql and val
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))   # success notification
    
insert_data(db)  # call insert_data function
