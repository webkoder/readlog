from google.cloud import bigquery
from google.oauth2 import service_account
from Registro import Registro
from Contador import Contador
credentials = service_account.Credentials.from_service_account_file( 'nobetabigquery.json' )

project_id = 'nobeta'
dataset = 'requisicoes'
client = bigquery.Client(credentials= credentials,project=project_id)


query = """select timestamp,
    httpRequest.requestUrl as url,
    httpRequest.userAgent as useragent,
    httpRequest.referer as referer,
    httpRequest.latency as latency,
    jsonpayload_type_loadbalancerlogentry.statusdetails as details,
    insertId, httpRequest.responseSize as size, httpRequest.status as status
 from `nobeta.scriptnobeta.requests_20210802` limit 50;"""

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
    item.contadorReferer()


for (key, item) in grupo.items():
    print( item )


# TODO criar uma tabela com os campos da classe contador e gravar 
# os mesmo, incluindo a data do consulta 


# Criar um job para fazer a chamada do main

# Criar uma tabela para gravar notificação de urls com caracteres especiais