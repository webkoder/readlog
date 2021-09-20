import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

try:
    con = mysql.connector.connect(host=host,database=database,user=user,password=password,unix_socket='')
    cursor = con.cursor()
except mysql.connector.Error as err:
    print (str(err))
    raise

def getCursor():
    try:
        con = mysql.connector.connect(host=host,database=database,user=user,password=password,unix_socket='')
        cursor = con.cursor()
    except mysql.connector.Error as err:
        print (str(err))
        raise

    return con, cursor
