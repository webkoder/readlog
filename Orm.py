from db import  cursor, con 

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
       cursor.executemany(sql,valores)

    @staticmethod
    def fecharCursor():
       cursor.close()
       con.commit()
       con.close()