import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('MYSQL_HOST')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DATABASE')

con = mysql.connector.connect(host=host,database=database,user=user,password=password)
cursor = con.cursor()