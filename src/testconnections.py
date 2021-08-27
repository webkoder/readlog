import os
from dotenv import load_dotenv
import mysql.connector
from google.cloud import bigquery
from google.oauth2 import service_account

def contest():
    load_dotenv()
    host = os.getenv('MYSQL_HOST')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    database = os.getenv('MYSQL_DATABASE')

    con = mysql.connector.connect(host=host,database=database,user=user,password=password)
    cursor = con.cursor()

    sites = ''
    cursor.execute("select * from site limit 5")
    
    myresult = cursor.fetchall()

    for x in myresult:
        sites +=  x[1] + ', '

    return sites


def bqtest():
    print( 'teste de conexão com banco de dados MySQL' )
    sites = contest()

    project_id = 'nobeta'
    path = os.path.dirname(os.path.realpath(__file__)) + os.sep
    credentials = service_account.Credentials.from_service_account_file( path + 'nobetabigquery.json' )
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


print ( bqtest() )