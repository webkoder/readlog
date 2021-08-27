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
