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

if db.is_connected():   # connect checked
    print("berhasil terhubung ke database")

else :
    exit()