from google.cloud import bigquery
from google.oauth2 import service_account
from Registro import Registro
from Contador import Contador
from Orm import Orm
from datetime import date, datetime,timedelta
import sys

credentials = service_account.Credentials.from_service_account_file( 'nobetabigquery.json' )

project_id = 'nobeta'
dataset = 'requisicoes'
client = bigquery.Client(credentials= credentials,project=project_id)

if len(sys.argv) == 1:
    data = date.today() - timedelta(days=1)
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
 from `nobeta.scriptnobeta.requests_"""+dataf+"""` limit 20;"""

query_job = client.query(query)

results = query_job.result()

# transforma o resultado em uma array de objetos
objetos = []
for row in results:
    o = Registro(row)
    objetos.append( o )


# agrupar por bloco
grupo = {}
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
 #   item.contadorReferer()
# Contar categoria por device
    item.contadorCategoria()


for (key, item) in grupo.items():
    item.data = data
    Orm.gravar(item.toTupla())
    print( item )

Orm.fecharCursor()


# TODO

# Criar tabela só para gravar refer
# Criar uma tabela para gravar notificação de urls com caracteres especiais