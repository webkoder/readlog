from Registro import Registro
from Contador import Contador
from mysqldata import MySQLData
from datetime import date, datetime,timedelta
import sys
from bigqueryclient import getClient
from dataparam import byRequest

def principal(tipo, adunit, data):
    client = getClient()

    dataf = data.replace('-', '')

    prefixtipo = 'https://api.nobeta.com.br/nobetaads&id=' if tipo == 'script' else 'https://cdn.nobeta.com.br/'

    query = """select timestamp,
        httpRequest.requestUrl as url,
        httpRequest.userAgent as useragent,
        httpRequest.referer as referer,
        httpRequest.latency as latency,
        jsonpayload_type_loadbalancerlogentry.statusdetails as details,
        insertId, httpRequest.responseSize as size, httpRequest.status as status
    from `nobeta."""+ tipo +"""nobeta.requests_"""+dataf+"""`
    where httpRequest.requestUrl like '""" + prefixtipo + adunit + """%'; """

    query_job = client.query(query)

    results = query_job.result()
    # transforma o resultado em uma array de objetos
    objetos = []
    c = 0
    a = 0
    for row in results:
        o = Registro(row, tipo)
        objetos.append( o )
        c += 1
        if( c == 1000 ):
            a += 1
            print (str(a*1000) + ' registros processados ('+adunit+')')
            c = 0

    print('Criado objetos de registros. Preparando o processamento ('+adunit+')')

    # agrupar por bloco
    contador = Contador( tipo, adunit )
    contador.data = data
    contador.dados = objetos

    # calcular média de latência por bloco
    contador.calculaMedia()
    # contar device e browser
    contador.contadorDeviceBrowser()
    # contar response/details
    contador.contadorResponse()
    # contar status httpr
    contador.contadorStatus()
    # calcular média e a soma de tamanho do script
    contador.calculaMediaScript()
    # Contar referer url geral
    contador.contadorReferer()
    # Contar categoria por device
    contador.contadorCategoria()

    db = MySQLData()
    db.gravaEstatistica( contador.dadosEstatistica() )
    # db.gravaAcesso( contador.dadosAcesso() )

    db.fecharCursor()

    return str( len(objetos) )

    # print ( res )
    return res
    # TODO
    # Criar uma tabela para gravar notificação de urls com caracteres especiais