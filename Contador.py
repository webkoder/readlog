import numpy as np
from datetime import datetime

class Contador:
    def __init__(self, tipo, bloco):
        self.tipo = tipo
        self.bloco = bloco
        self.dados = []
        self.device = {}
        self.browser = {}
        self.response = {}
        self.status = {}
        self.avgsize = 0
        self.sumsize = 0
        self.latency = 0.0
        self.referer = {}
        self.data = None


    def add( self, item ):
        self.dados.append( item )

    def __str__( self ):
        return self.bloco + ". " + \
              str(len( self.dados )) + " itens | " + \
               str(self.latencymobile) + " Mobile | " + \
               str(self.latencydesktop) + " Desktop | " + \
               str(self.device) + " Browser | " + \
               str(self.browser) + " Response | " + \
               str(self.response) + " Status | " + \
               str(self.status) + " Size Media| " + \
               str(self.avgsize) + " Size Soma| " + \
               str(self.sumsize) + " Url Geral| " + \
               str(self.referer) 

    def contadorCategoria( self ):
    
        mobile = 0
        desktop = 0
        outros  = 0
        for registro in self.dados:
            if  registro.categoria == 1:
                mobile += 1
            elif registro.categoria == 2:
                desktop += 1
            else:
                outros += 1
        self.categorias = {'mobile': mobile, 'desktop': desktop, 'outros': outros}
    
    def calculaMedia( self ):
    
        latenciaMobile = []
        latenciaDesktop = []
        for registro in self.dados:
            if  registro.categoria == 1:
                latenciaMobile.append(registro.latency)
            elif registro.categoria == 2:
                latenciaDesktop.append(registro.latency)

        if  not latenciaMobile:
            self.latencymobile = 0 
        else:
            self.latencymobile = np.average( latenciaMobile )
       
        if  not latenciaDesktop:
            self.latencydesktop = 0 
        else:
            self.latencydesktop = np.average( latenciaDesktop )

    def contadorDeviceBrowser( self ):

        for registro in self.dados:
            indexD = registro.device
            indexB = registro.browser

            if indexD not in self.device:
                self.device[indexD] = 0
            self.device[ indexD ] = self.device[ indexD ] +1

            if indexB not in self.browser:
                self.browser[indexB] = 0
            self.browser[ indexB ] = self.browser[ indexB ] +1

    def contadorResponse( self ):
        
        for registro in self.dados:
            index = registro.response

            if index not in self.response:
                self.response[index] = 0
            self.response[ index ] = self.response[ index ] +1

    def contadorStatus( self ):
        
        for registro in self.dados:
            index = registro.status

            if index not in self.status:
                self.status[index] = 0
            self.status[ index ] = self.status[ index ] +1

    def calculaMediaScript( self ):
        script = [ x.size is not None and x.size or 0  for x in self.dados ]
        
        self.avgsize = np.average( script )
        self.sumsize = np.sum( script )

    def contadorReferer( self ):
        
        for registro in self.dados:
            index = registro.referer

            if index not in self.referer:
                self.referer[index] = 0
            self.referer[ index ] = self.referer[ index ] +1
     
    def dadosEstatistica (self):
        return ( self.tipo, self.bloco, str(self.categorias), str(self.device), str(self.browser), str(self.response), str(self.status), float(self.avgsize), float(self.sumsize), float(self.latencymobile), float(self.latencydesktop),  self.data)

    def dadosAcesso (self):
        data = datetime.strptime(self.data,'%Y-%m-%d')
        ano = data.year
        mes = data.month

        lista = []
        for referer, contagem in self.referer.items():
            lista.append ((self.bloco,referer,contagem, mes, ano ))
        return lista 