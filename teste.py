import os
import json
import mysql.connector
from google.cloud import bigquery
from google.oauth2 import service_account

def contest(request):
    db = os.environ.get('MYSQLPY')
    db = json.loads(db)
    con = mysql.connector.connect(host=db['host'],database=db['database'],user=db['user'],password=db['password'])
    cursor = con.cursor()

    sites = ''
    cursor.execute("select * from site limit 5")
    
    myresult = cursor.fetchall()

    for x in myresult:
        sites +=  x[1] + ', '

    return sites


def bqtest(request):
    print( 'teste de conexão com banco de dados MySQL' )
    sites = contest(request)

    project_id = 'nobeta'
    credentials = service_account.Credentials.from_service_account_file( 'nobetabigquery.json' )
    client = bigquery.Client(credentials= credentials,project=project_id)
    query = """select timestamp,
        httpRequest.requestUrl as url,
        httpRequest.userAgent as useragent,
        httpRequest.referer as referer,
        httpRequest.latency as latency,
        jsonpayload_type_loadbalancerlogentry.statusdetails as details,
        insertId, httpRequest.responseSize as size, httpRequest.status as status
    from `nobeta.scriptnobeta.requests_20210824` limit 1 ;"""

    query_job = client.query(query)
    results = query_job.result()

    print( 'teste de conexão com BigQuery' )
    for row in results:
        return str(row[1]) + " | Sites " + sites


print ( bqtest(None) )