from db import  cursor, con 

class Orm:

    @staticmethod
    def gravar (valores):
       sql = "INSERT INTO estatistica ( bloco, device, browser, response, status,avgsize, sumsize, latencymobile, latencydesktop, categorias, referer, data )  VALUES \
       ( %s , %s , %s , %s ,%s , %s ,%s , %s ,%s , %s, %s, %s )"
       cursor.execute(sql,valores)


    @staticmethod
    def fecharCursor():
       cursor.close()
       con.commit()
       con.close()