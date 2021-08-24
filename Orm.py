from db import  cursor, con 
import mysql.connector

class Orm:

    @staticmethod
    def gravaEstatistica (valores):
       sql = "INSERT INTO estatistica ( bloco, categorias, device, browser, response, status, avgsize, sumsize, latencymobile, latencydesktop, data )  VALUES \
       ( %s , %s , %s , %s ,%s , %s ,%s , %s ,%s , %s, %s )"
       cursor.execute(sql,valores)

    @staticmethod
    def gravaAcesso (valores):
       sql = "INSERT INTO acesso ( bloco, referer, contagem, mes, ano )  VALUES \
       ( %s , %s , %s , %s ,%s )"

       for dados in valores: 
         try:
          cursor.execute(sql,dados)
         except mysql.connector.Error as err:
          print(dados)
      
    @staticmethod
    def fecharCursor():
       cursor.close()
       con.commit()
       con.close()