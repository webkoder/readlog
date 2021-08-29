from bigqueryclient import getClient

def test():
    client = getClient()    
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
        return str(row[1])