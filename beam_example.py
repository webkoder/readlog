import apache_beam as beam
from apache_beam.io.textio import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
# import re
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.io import ReadFromText
import json
from user_agents import parse 

# $ python main.py --temp_location=gs://loggingnobeta --project=nobeta
# def read_from_bigquery():
# table_spec = 'nobeta:scriptnobeta.requests_20210831'
table_spec = bigquery.TableReference(
    projectId='nobeta',
    datasetId='scriptnobeta',
    tableId='requests_20210830')

    
query = """select timestamp,
        httpRequest.requestUrl as url,
        httpRequest.userAgent as useragent,
        httpRequest.referer as referer,
        httpRequest.latency as latency,
        jsonpayload_type_loadbalancerlogentry.statusdetails as details,
        insertId, httpRequest.responseSize as size, httpRequest.status as status
    from nobeta.scriptnobeta.requests_20210829 limit 100 ;"""

def parseJson( el ):
    return json.loads( el )

def extractSite( el ):
    indexid = el['url'].index("&id=") + 4
    txt = el['url'][indexid:].replace('.inter', '')
    txt = txt.split('&')[0]
    if( isinstance( txt, str) is not True ):
        print( el )
        raise("erro ao obter o bloco de " + el['url'])
    el['bloco'] = getBloco(txt)
    return el

def getBloco(txt):
    if txt is None:
        return ''

    if len(txt) > 80:
        return txt[0:80]   
    return txt

def extractDate( el ):
    el['date'] = el['timestamp'].strftime("%Y-%m-%d")
    return el

def parserUserAgent( el ):
    try:
        useragent = parse (el['useragent'])
    except:
        print(el['useragent'])
        raise("erro ao converter o user agent")

    el['device'] = useragent.device.family

    el['browser'] = useragent.browser.family

    if useragent.is_mobile | useragent.is_tablet:
        el['categoria'] = 1
    elif useragent.is_pc:
        el['categoria'] = 2
    else:
        el['categoria'] = 3

    return el

def createKey( el ):
    return el['bloco'], el

def groupLatency( el ):
    

pipeline_options = PipelineOptions(argv=None)
pipeline = beam.Pipeline(options=pipeline_options)

requisicoes = (
    pipeline
    | 'Ler dataset ' >> beam.io.ReadFromBigQuery(query=query)
    | 'Extract Site' >> beam.Map( extractSite )
    | 'Extract Date' >> beam.Map( extractDate )
    | 'Extract User Agent' >> beam.Map( parserUserAgent )
    | 'Create bloco Key' >> beam.Map( createKey )
    | 'Extract latency' >> beam.Map( )
    | 'Combine keys' >> beam.GroupByKey( )
    | "Mostrar Resultados da união" >> beam.Map( print )
)

requisicoes = (
    pipeline
    # | 'Ler dataset ' >> beam.io.ReadFromBigQuery(query=query)
    | 'Ler mock' >> ReadFromText('mock.txt')
    | 'Parse json' >> beam.Map( parseJson )
    | 'Extrair o site' >> beam.Map( extractSite )
    # | 'Criar arquivo para teste' >> WriteToText('mock', file_name_suffix='.txt')
    | "Mostrar Resultados da união" >> beam.Map( print )
)


def trata_data( elemento ):
    elemento['ano_mes'] = '-'.join(elemento['data_iniSE'].split('-')[:2])
    return elemento

colunas_dengue = [
    'id',
    'data_iniSE',
    'casos',
    'ibge_code',
    'cidade',
    'uf',
    'cep',
    'latitude',
    'longitude'
]

def chave_uf_ano_mes_de_lista( elemento ):
    data, mm, uf = elemento
    chave = uf + '-' + '-'.join(data.split('-')[:2])
    if( float(mm) < 0):
        mm = 0.0
    else:
        mm = float(mm)
    return chave, mm

def lista_para_dicionario( elemento, colunas):
    return dict(zip(colunas, elemento))

def texto_para_linha( elemento, delimitador='|'):
    return elemento.split(delimitador)

def chave_uf( elemento ):
    chave = elemento['uf']
    return (chave, elemento)

def arredonda( elemento ):
    chave, mm = elemento
    return chave,round(mm,1)

def preparar_csv( elemento, delimitador=";" ):
    return delimitador.join( elemento )

def descompactar_elementos( elemento ):
    chave, dados = elemento
    chuva = dados['chuvas'][0]
    dengue = dados['dengue'][0]
    uf, ano, mes = chave.split('-')
    return (uf, ano, mes, str(chuva), str(dengue))

def filtra_campos_vazios(elemento):
    chave, dados = elemento
    if all([ dados['chuvas'], dados['dengue'] ]):
        return True
    return False

def casos_dengue(elemento):
    uf, registros = elemento # extrair elemento
    for registro in registros:
        if( bool(re.search( r'\d', registro['casos'] )) ):
            yield (f"{uf}-{registro['ano_mes']}", float(registro['casos'])) # yield generator
        else:
            yield (f"{uf}-{elemento['ano_mes']}", 0.0) # yield generator


dengue = (
    pipeline
    | "Ler arquivo de dengue" >> ReadFromText('sample_casos_dengue.txt', skip_header_lines=1)
    | "De texto para lista" >> beam.Map( texto_para_linha )
    | "Transformar lista para dicionario" >> beam.Map( lista_para_dicionario, colunas_dengue )
    | "Criar campo mes" >> beam.Map( trata_data )
    | "Criar chave pelo estado" >> beam.Map( chave_uf )
    | "Agrupar por estado" >> beam.GroupByKey()
    | "Descompactar casos de dengue" >> beam.FlatMap( casos_dengue ) # pois retorna um yeild
    | "Soma casos pela chave" >> beam.CombinePerKey( sum )
    # | "Mostrar Resultados de dengue" >> beam.Map( print )
)

chuvas = (
    pipeline
    | "Ler arquivo de chuva" >> ReadFromText('sample_chuvas.csv', skip_header_lines=1)
    | "De texto para lista (Chuvas)" >> beam.Map( texto_para_linha, delimitador=',' )
    | "Criando chave ano mes" >> beam.Map( chave_uf_ano_mes_de_lista )
    | "Mostrar resultados de chuvas" >> beam.CombinePerKey(sum)
    | "Arredondar resultados" >> beam.Map( arredonda )
    # | "Mostrar Resultados de chuva" >> beam.Map( print )

)


resultado = (
    # ( chuva, dengue )
    # | "Empilha as pcollections" >> beam.Flatten()
    # | "Agrupa as pcol" >> beam.GroupByKey()
    ({'chuvas': chuvas, 'dengue': dengue})
    | "Mesclar pcols" >> beam.CoGroupByKey()
    | "Filtrar dados vazios" >> beam.Filter( filtra_campos_vazios )
    | "Descompactar elementos" >> beam.Map( descompactar_elementos )
    | "Preparar CSV" >> beam.Map( preparar_csv)
    # | "Mostrar Resultados da união" >> beam.Map( print )
)

header='UF;ANO;MES;CHUVA;DENGUE'
resultado | 'Criar arquivo CSV' >> WriteToText('resultado', file_name_suffix='.csv', header=header)

