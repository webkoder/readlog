from user_agents import parse 
from TrataCampos import TrataCampos


class Registro:
    def __init__(self, row, tipo):
        self.tipo = tipo
        self.tratador = TrataCampos(row)
        self.timestamp = row[0]
        
        self.url = self.tratador.getUrl()

        self.useragent = self.tratador.getUseragent()
        self.referer = self.tratador.getReferer()
        self.latency = self.tratador.getLatency()
        self.response = self.tratador.getResponse()
        self.id = self.tratador.getId()
        self.size = self.tratador.getSize()
        self.status = self.tratador.getStatus()

        self.bloco = 'nao-inicializado'
        self.browser = 'nao-inicializado'
        self.device = 'nao-inicializado'
        
        if( tipo == 'script'):
            self.extractSite()
        else:
            self.extractSiteCdn()
        self.extractDate()
        self.parserUserAgent()
          

    def parserUserAgent(self):
        try:
            useragent = parse (self.useragent)
        except:
            print(self.useragent)
            raise("erro ao converter o user agent")

        self.device = useragent.device.family

        self.browser = useragent.browser.family

        if useragent.is_mobile | useragent.is_tablet:
            self.categoria = 1
        elif useragent.is_pc:
            self.categoria = 2
        else:
            self.categoria = 3 


    def __str__(self) -> str:
        try:
            response = self.bloco + " | " + \
               self.useragent + " | " + \
               self.url + " | " + \
               self.response + " | " + \
               self.date + " | " + \
               self.device + " | " + \
               self.browser + " | " + \
               str(self.latency) + " | " + \
               self.referer
        except:
            print( self.id )
            raise("erro na concatenaçao")
        return response

    def extractDate(self):
        self.date = self.timestamp.strftime("%Y-%m-%d")

    def extractSite(self):
        indexid = self.url.index("&id=") + 4
        txt = self.url[indexid:].replace('.inter', '')
        txt = txt.split('&')[0]
        if( isinstance( txt, str) is not True ):
            print( self )
            raise("erro ao obter o bloco de " + self.url)
        self.bloco = self.tratador.getBloco(txt)
        
    def extractSite(self):
        indexid = self.url.index("&id=") + 4
        txt = self.url[indexid:].replace('.inter', '')
        txt = txt.split('&')[0]
        if( isinstance( txt, str) is not True ):
            print( self )
            raise("erro ao obter o bloco de " + self.url)
        self.bloco = self.tratador.getBloco(txt)