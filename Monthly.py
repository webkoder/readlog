class Monthly:
    def __init__(self, site):
        self.site = site
        self.registros = 0
        self.data = []

    def add( self, item ):
        self.registros += 1
        self.data.append( item )

    def __str__(self) -> str:
        return self.site + ' ' + str(self.registros)

#         SQL Error [1366] [HY000]: Incorrect string value: '\xC4\x8D': 1...' for column 'browser' at row 1
#   Incorrect string value: '\xC4\x8D': 1...' for column 'browser' at row 1
#   Incorrect string value: '\xC4\x8D': 1...' for column 'browser' at row 1
