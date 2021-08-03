import numpy as np

class Contador:
    def __init__(self, bloco):
        self.bloco = bloco
        self.dados = []
        self.device = {}
        self.browser = {}
        self.response = {}


    def add( self, item ):
        self.dados.append( item )

    def __str__( self ):
        return self.bloco + ". " + \
               str(len( self.dados )) + " itens | " + \
               str(self.latency) + " Device | " + \
               str(self.device) + " Browser | " + \
               str(self.browser) + " Response | " + \
               str(self.response) 

    def calculaMedia( self ):
        latencias = [ x.latency for x in self.dados ]
        self.latency = np.average( latencias )

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

     