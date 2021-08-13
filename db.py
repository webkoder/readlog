import mysql.connector

con = mysql.connector.connect(host='localhost',database='nobeta',user='root',password='1122')
cursor = con.cursor()