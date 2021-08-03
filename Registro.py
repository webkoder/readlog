import httpagentparser

class Registro:
    def __init__(self, row):
        self.timestamp = row[0]
        self.url = row[1]
        self.useragent = row[2]
        self.referer = row[3]
        self.latency = row[4]
        self.response = row[5]
        self.id = row[6]

        self.parserUserAgent()
        self.extractSite()
        self.extractDate()

    def parserUserAgent(self):
        useragent = httpagentparser.simple_detect(self.useragent)
        self.device = useragent[0]
        self.browser = useragent[1]

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