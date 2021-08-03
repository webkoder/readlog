import numpy as np

class Contador:
    def __init__(self, bloco):
        self.bloco = bloco
        self.dados = []

    def add( self, item ):
        self.dados.append( item )

    def __str__( self ):
        return self.bloco + ". " + \
               str(len( self.dados )) + " itens | " + \
               str(self.latency)

    def calculaMedia( self ):
        latencias = [ x.latency for x in self.dados ]
        self.latency = np.average( latencias )