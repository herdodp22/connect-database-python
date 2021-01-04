import mysql.connector   # import module connector
import os      # import ose

database = mysql.connector.connect(    
    host = 'localhost',  # host 
    user = 'root',   # user  ( xampp )
    password = '',  # password
    database = 'db_careio' # database name ( fill with your database name)
)

if database.is_connected():   # connect checked
    print("berhasil terhubung ke database")

else :
    exit()