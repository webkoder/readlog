urls = [
    'https://api.nobeta.com.br/nobetaads&id=maisnovela.inter',
    'https://api.nobeta.com.br/nobetaads&id=maisnovela',
    'https://api.nobeta.com.br/nobetaads&id=maisnovela.inter&f=alert,inter',
    'https://api.nobeta.com.br/nobetaads&id=maisnovela&f=alert,inter',
    'https://api.nobeta.com.br/nobetaads&id=jornaldefato.blogspot.inter',
    'https://api.nobeta.com.br/nobetaads&id=jornaldefato.blogspot.inter&f=alert,inter'
]

for url in urls:
    indexid = url.index("&id=") + 4
    txt = url[indexid:].replace('.inter', '')
    txt = txt.split('&')[0]
    print( txt )