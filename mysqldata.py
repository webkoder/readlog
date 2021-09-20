# from db import getCursor 
# import mysql.connector

from db import getCursor


class MySQLData:

   def __init__( self ):
      from db import getCursor
      d = getCursor()
      self.con = d[0]
      self.cursor = d[1]

   # @staticmethod
   # def gravaEstatistica (valores):
   #    sql = "INSERT INTO estatistica ( bloco, categorias, device, browser, response, status, avgsize, sumsize, latencymobile, latencydesktop, data )  VALUES \
   #    ( %s , %s , %s , %s ,%s , %s ,%s , %s ,%s , %s, %s )"
   #    cursor.execute(sql,valores)

   # @staticmethod
   # def gravaAcesso (valores):
   #    sql = "INSERT INTO acesso ( bloco, referer, contagem, mes, ano )  VALUES \
   #    ( %s , %s , %s , %s ,%s )"

   #    for dados in valores: 
   #       try:
   #          cursor.execute(sql,dados)
   #       except mysql.connector.Error as err:
   #          print(dados)

   def getData( self, date ):
      # o parametro bind %s não está funcionando, descobrir o motivo
      sql = ("SELECT bloco FROM estatistica WHERE data = '"+date+"'")
      self.cursor.execute( sql, (date) )

      data = []
      for bloco in self.cursor:
         data.append(bloco[0])

      self.fecharCursor()
      return data
      
   def fecharCursor( self ):
      self.cursor.close()
      self.con.commit()
      self.con.close()