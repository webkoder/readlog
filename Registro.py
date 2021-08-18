from user_agents import parse 


class Registro:
    def __init__(self, row):
        self.timestamp = row[0]
        self.url = row[1]
        self.useragent = row[2]
        self.referer = row[3]
        self.latency = row[4]
        self.response = row[5]
        self.id = row[6]
        self.size = row[7]
        self.status = row[8] 

        self.validar()
        #self.parserUserAgent()
        self.extractSite()
        self.extractDate()

    def validar(self):
        if self.referer is None:
            return
        if self.useragent is None:
            return

        if len(self.referer) > 512:
            print(self.referer)
            raise Exception('Erro! ')

    def parserUserAgent(self):
        useragent = parse (self.useragent)
        self.device = useragent.device.family

        self.browser = useragent.browser.family

        if useragent.is_mobile | useragent.is_tablet:
            self.categoria = 1
        elif useragent.is_pc:
            self.categoria = 2
        else:
            self.categoria = 3 


    def __str__(self) -> str:
        return self.bloco + " | " + \
               self.date + " | " + \
               self.device + " | " + \
               self.browser + " | " + \
               str(self.latency) + " | " + \
               self.referer

    def extractDate(self):
        self.date = self.timestamp.strftime("%Y-%m-%d")

    def extractSite(self):
        indexid = self.url.index("&id=") + 4
        txt = self.url[indexid:].replace('.inter', '')
        txt = txt.split('&')[0]
        self.bloco = txt