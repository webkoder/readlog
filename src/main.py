from google.cloud import bigquery
from google.oauth2 import service_account # descomentar para teste local
from Registro import Registro
from Contador import Contador
from Orm import Orm
from datetime import date, datetime,timedelta
import sys
import os

def principal(request):
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    credentials = service_account.Credentials.from_service_account_file( path + 'nobetabigquery.json' )

    project_id = 'nobeta'
    client = bigquery.Client(credentials= credentials,project=project_id)

    if len(sys.argv) == 1:
        data = date.today()  - timedelta(days=1)
    else:
        data = datetime.strptime(sys.argv[1],'%Y-%m-%d')

    dataf = data.strftime('%Y%m%d')

    query = """select timestamp,
        httpRequest.requestUrl as url,
        httpRequest.userAgent as useragent,
        httpRequest.referer as referer,
        httpRequest.latency as latency,
        jsonpayload_type_loadbalancerlogentry.statusdetails as details,
        insertId, httpRequest.responseSize as size, httpRequest.status as status
    from `nobeta.scriptnobeta.requests_"""+dataf+"""` """

    query_job = client.query(query)

    results = query_job.result()
    print('Dados obtidos. ' + dataf)
    # transforma o resultado em uma array de objetos
    objetos = []
    c = 0
    a = 0
    for row in results:
        o = Registro(row)
        objetos.append( o )
        c += 1
        if( c == 1000 ):
            a += 1
            print (str(a*1000) + ' registros processados')
            c = 0

    print('Criado objetos de registros. Preparando o processamento ')

    # agrupar por bloco
    grupo = {}
    c=0
    for objeto in objetos:
        index = objeto.bloco

        if index not in grupo:
            grupo[ index ] = Contador( index )

        grupo[ index ].add( objeto )

    for (key, item) in grupo.items():
    # calcular média de latência por bloco
        item.calculaMedia()
    # contar device e browser
        item.contadorDeviceBrowser()
    # contar response/details
        item.contadorResponse()
    # contar status http
        item.contadorStatus()
    # calcular média e a soma de tamanho do script
        item.calculaMediaScript()
    # Contar referer url geral
        item.contadorReferer()
    # Contar categoria por device
        item.contadorCategoria()
        print (str(c) + ' site processado')
        c += 1

    c = 0
    for (key, item) in grupo.items():
        item.data = data
        Orm.gravaEstatistica(item.dadosEstatistica())
        Orm.gravaAcesso(item.dadosAcesso())
        print (str(c) + ' site gravado')
        c += 1

    Orm.fecharCursor()

    res = 'finalizado com ' + str( len(grupo) ) + ' sites gravados.'
    res += ' Dia do dataset: ' + dataf

    # print ( res )
    return res
    # TODO
    # Criar uma tabela para gravar notificação de urls com caracteres especiais