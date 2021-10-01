class TrataCampos:
    def __init__(self, valores):
        self.valores = valores

    def getUrl(self):
        if self.valores[1] is None:
            return ''
        return self.valores[1]

    def getUseragent(self):
        if self.valores[2] is None:
            return ''
        return self.valores[2]

    def getReferer(self):
        if self.valores[3] is None:
            return ''
        
        if len(self.valores[3]) > 512:
            return self.valores[3][0:512]   
        return self.valores[3]

    def getLatency(self):
        if self.valores[4] is None:
            return 0
        return self.valores[4]

    def getResponse(self):
        if self.valores[5] is None:
            return ''
        return self.valores[5]

    def getId(self):
        if self.valores[6] is None:
            return ''
        return self.valores[6]

    def getSize(self):
        if self.valores[7] is None:
            return 0
        return self.valores[7]

    def getStatus(self):
        if self.valores[8] is None:
            return ''
        return self.valores[8]

    def getBloco(self,txt):
        if txt is None:
            return ''

        if len(txt) > 80:
            return txt[0:80]   
        return txt 

    @staticmethod
    def extractBlocoCdn( txt ):
        txt = txt.replace('https://cdn.nobeta.com.br/', '')
        
        # vazio
        if len( txt ) == 0:
            return 'outros'

        # identificar tag iab.min.js
        if txt == 'iab.min.js':
            return txt

        # identificar assinaturas
        x = re.search("^sign/.*/(.*)\.", txt)
        if x is not None:
            res = x[1].replace('sign_', '')
            return 'sign-' + res

        x = re.search("^sign/(.*)\.", txt)
        if x is not None:
            res = x[1].replace('sign_', '')
            return 'sign-' + res

        # idenfificar tag iab de parceiro
        x = re.search("^iab-(.*)\.min\.js", txt)
        if x is not None:
            return x[1]

        # identificar versão cdn da tag nobeta
        x = re.search("^sign/(.*)\.", txt)
        if x is not None:
            return x[1]

        # midia kit
        if txt == 'midia/midiakit_2020_nobeta.pdf':
            return 'midia'

        # agrupar se não encaixar em nenhum item
        return 'outros'