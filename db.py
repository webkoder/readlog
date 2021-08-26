import mysql.connector
import os
import json

db = os.environ.get('MYSQLPY')
db = json.loads(db)
con = mysql.connector.connect(host=db['host'],database=db['database'],user=db['user'],password=db['password'], unix_socket="/cloudsql/nobeta:us-west1:mysql-nobeta-prd")
cursor = con.cursor()